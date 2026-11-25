from flask import render_template, request, redirect, url_for, session, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/auth/static')

@auth_bp.route('/cadastroForm', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        nomeUsuario = request.form.get('nomeUsuario')
        nomeCompleto = request.form.get('nomeCompleto')
        email = request.form.get('email')
        dataNascimento = request.form.get('dataNascimento')
        senha = request.form.get('senha')
        confirmacaoSenha = request.form.get('confirmacaoSenha')

        if senha != confirmacaoSenha:
            flash('As senhas não coincidem!')

        if len(senha) < 8:
            flash('A senha deve ter pelo menos 8 caracteres!')

        senhaHash = generate_password_hash(senha)

        try:
            connection = get_db()
            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT id FROM usuarios
                    WHERE email = %s
                """, (email,))

                emailExistente = cursor.fetchone()

                if emailExistente:
                    flash('Esse email já está cadastrado!')

                sql = """
                    INSERT INTO usuarios (nomeUsuario, nomeCompleto, email, dataNascimento, senha) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (nomeUsuario, nomeCompleto, email, dataNascimento, senhaHash))
                connection.commit()

                return redirect(url_for('auth.login'))

        except Exception as e:
            flash(f'Erro ao cadastrar: {e}')
        finally:
            connection.close()

    return render_template('cadastroForm.html')

@auth_bp.route('/loginForm', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        try:
            connection = get_db()
            with connection.cursor() as cursor:
                sql = "SELECT * FROM usuarios WHERE email = %s"
                cursor.execute(sql, (email,))
                usuario = cursor.fetchone()

                if usuario and check_password_hash(usuario['senha'], senha):

                    session.clear()

                    session['usuarioId'] = usuario['id']
                    session['nomeUsuario'] = usuario['nomeUsuario']

                    return redirect(url_for('homepage.homepage'))

                else:
                    flash("Email ou senha Incorretos!")

        except Exception as e:
            flash(f'Erro ao fazer login: {e}')
        finally:
            connection.close()

    return render_template('loginForm.html')
