from flask import Blueprint, render_template

# Create Blueprint
views = Blueprint('views', __name__)

# route
@views.route('/')
def home() :
    return render_template('home.html')
