from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import db

# Create Blueprint
views = Blueprint('views', __name__)

# route
@views.route('/', methods = ['GET','POST'])
@login_required
def home() :
    return render_template('home.html')
