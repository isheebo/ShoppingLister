from flask import Blueprint, request, flash, redirect, render_template, url_for, session
from models.user import User
from models.shoppinglist import ShoppingList
from models.item import Item
from models.mainapp import App

lister = Blueprint("lister", __name__)

app_instance = App()


@lister.route("/")
@lister.route("/signup", methods=['GET', 'POST'])
def signup():
    """ Defines routes for signing up a new user. """
    error = None

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("signup.html", error="Password mismatch! please try again")

        if name and email and password and confirm_password:
            user = User(name, email, password)
            # if a user has just been registered, then, ...
            if app_instance.register(user):
                flash("You have been registered")
                return redirect(url_for("lister.login"))
            error = f"User with email \"{email}\" already exists!!, try logging in"
    return render_template("signup.html", error=error)
