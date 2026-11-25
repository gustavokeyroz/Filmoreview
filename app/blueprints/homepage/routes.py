from flask import render_template, Blueprint
from app.db import get_db

homepage_bp = Blueprint('homepage', __name__, template_folder='templates', static_folder='static', static_url_path='/homepage/static')

@homepage_bp.route('/')
def homepage():

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

            filmes = cursor.fetchall()

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
            LIMIT 10
""")

            posts = cursor.fetchall()

        return render_template(
            'homepage.html',
            filmes=filmes,
            posts=posts
        )

    finally:
        connection.close()