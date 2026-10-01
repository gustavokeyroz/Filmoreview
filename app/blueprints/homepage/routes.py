from flask import Blueprint, render_template, redirect

homepage_bp = Blueprint('homepage', __name__, template_folder='templates')

@homepage_bp.route('/')
def homepage():
    return render_template('homepage.html')