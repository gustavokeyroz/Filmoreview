from flask import render_template, Blueprint, redirect, url_for, session, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

perfil_bp = Blueprint('perfil', __name__, template_folder='templates', static_folder='static', static_url_path='/perfil/static')

@perfil_bp.route('/perfil', methods=['GET'])
def perfil():

    if 'usuarioId' not in session:
        return redirect(url_for('auth.login'))

    try:
        connection = get_db()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, nomeCompleto, nomeUsuario, email FROM usuarios WHERE id = %s
""", (session['usuarioId'],))

            usuario = cursor.fetchone()

            if not usuario:
                session.clear()
                return redirect(url_for('auth.login'))

            return render_template('perfil.html', usuario=usuario)

    finally:
        connection.close()

@perfil_bp.route('/perfil/alterarSenha', methods=['POST'])
def alterarSenha():
    if 'usuarioId' not in session:
        return redirect(url_for('auth.login'))

    senhaAtual = request.form.get('senhaAtual', '')
    novaSenha = request.form.get('novaSenha', '')
    confirmarNovaSenha = request.form.get('confirmarNovaSenha', '')

    if not senhaAtual or not novaSenha or not confirmarNovaSenha:
        flash('Preencha todos os campos!')
        return redirect(url_for('perfil.perfil'))

    if novaSenha != confirmarNovaSenha:
        flash('As senhas não coincidem!')
        return redirect(url_for('perfil.perfil'))

    if len(novaSenha) < 8:
        flash('A senha deve ter pelo menos 8 caracteres!')
        return redirect(url_for('perfil.perfil'))

    connection = get_db()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT senha FROM usuarios WHERE id = %s",
                (session['usuarioId'],)
            )
            usuario = cursor.fetchone()

            if not usuario or not check_password_hash(usuario['senha'], senhaAtual):
                flash('Senha atual incorreta!')
                return redirect(url_for('perfil.perfil'))

            senhaHash = generate_password_hash(novaSenha)

            cursor.execute(
                "UPDATE usuarios SET senha = %s WHERE id = %s",
                (senhaHash, session['usuarioId'])
            )

            connection.commit()

        flash('Senha alterada com sucesso!')
        return redirect(url_for('perfil.perfil'))

    finally:
        connection.close()

@perfil_bp.route('/perfil/alterarEmail', methods=['POST'])
def alterarEmail():
    if 'usuarioId' not in session:
        return redirect(url_for('auth.login'))

    novoEmail = request.form.get('novoEmail', '').strip()
    confirmarNovoEmail = request.form.get('confirmarNovoEmail', '').strip()
    senha = request.form.get('senha', '')

    if not novoEmail or not confirmarNovoEmail or not senha:
        flash('Preencha todos os campos!')
        return redirect(url_for('perfil.perfil'))

    if novoEmail != confirmarNovoEmail:
        flash('Os emails não coincidem!')
        return redirect(url_for('perfil.perfil'))

    connection = get_db()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT senha FROM usuarios WHERE id = %s",
                (session['usuarioId'],)
            )
            usuario = cursor.fetchone()

            if not usuario or not check_password_hash(usuario['senha'], senha):
                flash('Senha atual incorreta!')
                return redirect(url_for('perfil.perfil'))

            cursor.execute(
                "SELECT id FROM usuarios WHERE email = %s AND id != %s",
                (novoEmail, session['usuarioId'])
            )
            emailExistente = cursor.fetchone()

            if emailExistente:
                flash('Esse email já está cadastrado!')
                return redirect(url_for('perfil.perfil'))

            cursor.execute(
                "UPDATE usuarios SET email = %s WHERE id = %s",
                (novoEmail, session['usuarioId'])
            )

            connection.commit()

        flash('Email alterado com sucesso!')
        return redirect(url_for('perfil.perfil'))

    finally:
        connection.close()

@perfil_bp.route('/perfil/excluirPerfil', methods=['POST'])
def excluirPerfil():
    if 'usuarioId' not in session:
        return redirect(url_for('auth.login'))

    senha = request.form.get('senha', '')
    usuarioId = session['usuarioId']

    if not senha:
        flash('Informe sua senha!')
        return redirect(url_for('perfil.perfil'))

    connection = get_db()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT senha FROM usuarios WHERE id = %s",
                (usuarioId,)
            )
            usuario = cursor.fetchone()

            if not usuario or not check_password_hash(usuario['senha'], senha):
                flash('Senha incorreta!')
                return redirect(url_for('perfil.perfil'))

            cursor.execute(
                "DELETE FROM reviewFilmes WHERE fkIdUsuario = %s",
                (usuarioId,)
            )

            cursor.execute(
                "DELETE FROM usuarios WHERE id = %s",
                (usuarioId,)
            )

            connection.commit()

        session.clear()
        flash('Conta excluída com sucesso!')
        return redirect(url_for('auth.login'))

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

@perfil_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))