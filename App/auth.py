from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again", category="error")
        else:
            flash("User does not exist, try again", category="error")

    return render_template("Login.html", text="testing", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exist, Try another one!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(name) < 2:
            flash("Name must be greater than 2 characters.", category="error")
        elif password != password2:
            flash("Password1 and password2 must be equal.", category="error")
        elif len(password) < 7:
            flash("Password must greater than 7 characters.", category="error")
        else:
            new_user = User(
                email=email,
                name=name,
                password=generate_password_hash(password),
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category="success")

    return render_template("Signup.html", user=current_user)


@auth.route("/profile")
@login_required
def profile():
    return render_template("Profile.html", user=current_user)
