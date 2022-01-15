from flask import url_for, render_template, flash, redirect, request, session
# from main.forms import Registration, Login, RequestReset, ResetPassword, Update, Cohorts
from flask_login import login_user, current_user, logout_user, login_required
from main import app, bcrypt


# Home
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


# Data Analysis
@app.route('/data-analysis')
def data_analysis():
    return render_template('datanalysis.html')


# About
@app.route('/about')
def about():
    return render_template('data.html')


# Applications
@app.route('/applications')
def applications():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = Registration()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    return render_template('applications.html')


# Events
@app.route('/events')
def events():
    return render_template('events.html')