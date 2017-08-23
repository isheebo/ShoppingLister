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


@lister.route("/login", methods=["GET", "POST"])
def login():
    """
    Login is the entry point of the application. Without logging in,
    the core functionality of this application remains hidden.
    The route `/login` is used for this cause.
    """

    # if user is already logged in, redirect them to the home page.
    if session.get("logged_in"):
        return redirect(url_for("lister.shopping_list"))

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email and password:
            if app_instance.login(email, password):
                session["logged_in"] = True
                session['email'] = email
                return redirect(url_for("lister.shopping_list"))
            error = "Wrong email or password. Try Again"
            return render_template("login.html", error=error)
    return render_template("login.html")


@lister.route("/view/list")
def shopping_list():
    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))
    user = app_instance.get_user(session["email"])
    return render_template("shopping_list.html", shoppinglists=user.shoppinglists, user=user)
