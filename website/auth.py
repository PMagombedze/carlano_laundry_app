from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/signin')
def login():
    render_template('/auth/login.html')

@auth.route('/logout')
def logout():
    pass

@auth.route('/signup')
def signup():
    render_template('/auth/signup.html')
