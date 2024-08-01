import datetime

import pandas as pd
from wtforms.validators import ValidationError
from project import app, db
from flask import render_template, redirect, url_for, flash, request, Flask, jsonify

from project.algo import setupclists, filler, ListofSubs, Userinf, setupinf
from project.models import User, Choices
from project.forms import Register, SignIn, makeChoice
from flask_login import login_user, current_user
from project.algo import ListofNames, ListofSubs
from datetime import datetime as dt
import datetime

# returns the home page
@app.route("/")
def index():
    return render_template('index.html')


# it creates an account for a new user
@app.route("/register", methods=['GET', 'POST'])
def register():
    # the Register() form from forms.py is called
    form = Register()
    # if the form submitted the user will be added to user table
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # to let user to log in
        login_user(user)
        flash('You are registered!', category='info')
        return render_template("index.html")

    if form.errors != {}:
        for error in form.errors.values():
            flash(error, category='danger')

    return render_template('register.html', form=form)


# if user already have an account, user just needs to sign in
@app.route("/signIn", methods=['GET', 'POST'])
def signIn():
    # the SignIn() form from forms.py is called
    form = SignIn()

    # if the form submitted the user will be signed in
    if form.validate_on_submit():
        # the username should be unique, so it can be filtered by username
        user = User.query.filter_by(username=form.username.data).first()
        # if user exists and entered the correct password, user can log in
        if user and user.check_password(password=form.password.data):
            login_user(user)
            if "student" in user.email:
                # flash('You are signed in!', category='info')
                flash('Signed into student blackboard!', category='info')
                return redirect(url_for('studchoices'))
            else:
                return redirect((url_for("Teacher_Account")))

        else:
            flash('Invalid username or invalid password!', category='danger')
    return render_template('signIn.html', form=form)


@app.route("/teacheracc", methods=['GET', 'POST'])
def Teacher_Account():
    if request.method == "GET":
        return render_template("teacherpage.html")
    else:
        file = request.files["Excel"]
        df1 = pd.read_excel(file)
        excelfile = df1.to_numpy().tolist()
        print(excelfile)
        #setupclists(excelfile)
        #filler(ListofSubs, ListofNames, excelfile)
        setupinf(excelfile)
        return render_template("teacherpage.html")


@app.route("/studchoices", methods=['GET', 'POST'])
def studchoices():
    due = datetime.datetime(2022, 3, 15, 18, 00)
    form = makeChoice()
    if form.validate_on_submit():
        if due > dt.today():
            stud_choice = Choices(username=form.username.data, first_choice=form.first_choice.data,
                                    second_choice=form.second_choice.data, third_choice=form.third_choice.data)
            db.session.add(stud_choice)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('The date to make your choices has passed', category='danger')
            return redirect(url_for('studchoices'))

    if form.errors != {}:
        for error in form.errors.values():
            flash(error, category='danger')
    return render_template("student_choices.html", form=form)








































