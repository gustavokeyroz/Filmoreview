from flask import (
    render_template, request, redirect,
    url_for, session, Blueprint, flash
)
from app.db import get_db

filmes_bp = Blueprint(
    'filmes',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/filmes/static'
)


# Listagem de filmes
@filmes_bp.route('/filmes')
def filmes():

    connection = get_db()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT
                    filmes.id,
                    filmes.nomeFilme,
                    filmes.imageUrl,
                    COALESCE(AVG(reviewFilmes.nota), 0) AS mediaNota
                FROM filmes
                LEFT JOIN reviewFilmes
                    ON filmes.id = reviewFilmes.fkIdFilme
                GROUP BY
                    filmes.id,
                    filmes.nomeFilme,
                    filmes.imageUrl
                ORDER BY mediaNota DESC
                LIMIT 10
            """)

            filmesMaisBemAvaliados = cursor.fetchall()

            cursor.execute("""
                SELECT * FROM filmes
            """)

            filmes = cursor.fetchall()

        return render_template(
            'filmes.html',
            filmes=filmes,
            filmesMaisBemAvaliados=filmesMaisBemAvaliados
        )

    finally:
        connection.close()


# Detalhes do filme
@filmes_bp.route('/filme/<int:id>')
def detalheFilme(id):

    connection = get_db()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT * FROM filmes
                WHERE id = %s
            """, (id,))

            filme = cursor.fetchone()

            if not filme:
                return 'Filme não encontrado!', 404

            cursor.execute("""
                SELECT
                    reviewFilmes.nota,
                    reviewFilmes.comentario,
                    reviewFilmes.created_at,
                    usuarios.nomeUsuario
                FROM reviewFilmes
                JOIN usuarios
                    ON reviewFilmes.fkIdUsuario = usuarios.id
                WHERE reviewFilmes.fkIdFilme = %s
                ORDER BY reviewFilmes.created_at DESC
            """, (id,))

            postagens = cursor.fetchall()

        return render_template(
            'detalheFilme.html',
            filme=filme,
            postagens=postagens
        )

    finally:
        connection.close()


# Criar avaliação
@filmes_bp.route('/filme/<int:id>/avaliar', methods=['POST'])
def criarPostagem(id):

    if 'usuarioId' not in session:
        return redirect(url_for('auth.login'))

    nota = request.form.get('nota', type=int)
    comentario = request.form.get('comentario', '').strip()

    if nota not in [1, 2, 3, 4, 5]:
        flash('Selecione uma nota válida.')
        return redirect(url_for('filmes.detalheFilme', id=id))

    if not comentario or len(comentario) > 255:
        flash('O comentário deve ter entre 1 e 255 caracteres.')
        return redirect(url_for('filmes.detalheFilme', id=id))

    connection = get_db()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT id FROM filmes
                WHERE id = %s
            """, (id,))

            if not cursor.fetchone():
                return 'Filme não encontrado!', 404

            cursor.execute("""
                SELECT id FROM reviewFilmes
                WHERE fkIdUsuario = %s
                AND fkIdFilme = %s
            """, (session['usuarioId'], id))

            if cursor.fetchone():
                flash('Você já avaliou este filme.')
                return redirect(url_for('filmes.detalheFilme', id=id))

            cursor.execute("""
                INSERT INTO reviewFilmes
                (nota, comentario, fkIdFilme, fkIdUsuario)
                VALUES (%s, %s, %s, %s)
            """, (nota, comentario, id, session['usuarioId']))

            connection.commit()

        flash('Avaliação publicada!')

        return redirect(url_for('filmes.detalheFilme', id=id))

    finally:
        connection.close()