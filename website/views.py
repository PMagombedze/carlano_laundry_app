from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint("views", __name__)


@views.route('/')
@views.route('/home')
def home():
    """home template"""
    return render_template('index.html')


@views.route('/app/dashboard')
@login_required
def dashboard():
    """dashboard template"""
    return render_template('dashboard.html', user=current_user)
