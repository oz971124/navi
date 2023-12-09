from flask import Blueprint, render_template

# Create Blueprint
auth = Blueprint('auth', __name__)

# route
@auth.route('/log-in')
def log_in() :
    return render_template('log_in.html')

@auth.route('/log-out')
def log_out() :
    return render_template('log_out.html')

@auth.route('/sign-up')
def sign_in() :
    return render_template('sign_up.html')