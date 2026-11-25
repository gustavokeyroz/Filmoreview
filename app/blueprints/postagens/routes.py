from flask import render_template, Blueprint
from app.db import get_db

postagens_bp = Blueprint(
    'postagens',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/postagens/static'
)


@postagens_bp.route('/postagens')
def postagens():

    connection = get_db()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT
                    reviewFilmes.id,
                    reviewFilmes.nota,
                    reviewFilmes.comentario,
                    reviewFilmes.created_at,
                    usuarios.nomeUsuario,
                    filmes.nomeFilme,
                    filmes.id AS filmeId
                FROM reviewFilmes
                JOIN usuarios
                    ON reviewFilmes.fkIdUsuario = usuarios.id
                JOIN filmes
                    ON reviewFilmes.fkIdFilme = filmes.id
                ORDER BY reviewFilmes.created_at DESC
            """)

            posts = cursor.fetchall()

        return render_template('posts.html', posts=posts)

    finally:
        connection.close()