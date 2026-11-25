import os
from flask import Flask
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv('FLASK_SECRET_KEY')
    app.permanent_session_lifetime = timedelta(days=7)

    from app.blueprints.homepage.routes import homepage_bp
    from app.blueprints.auth.routes import auth_bp
    from app.blueprints.filmes.routes import filmes_bp
    from app.blueprints.perfil.routes import perfil_bp
    from app.blueprints.postagens.routes import postagens_bp

    app.register_blueprint(homepage_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(filmes_bp)
    app.register_blueprint(perfil_bp)
    app.register_blueprint(postagens_bp)

    return app