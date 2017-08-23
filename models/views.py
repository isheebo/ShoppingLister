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


@lister.route("/add/list", methods=["POST"])
def add_list():
    """ Defines routes for adding new shopping lists to the application. """
    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))
    user = app_instance.get_user(session["email"])
    name = request.form["name"]
    notify_date = request.form["notify_date"]
    if name and notify_date:
        list_id = app_instance.generate_ID()
        if user.create_shoppinglist(ShoppingList(list_id, name, notify_date)):
            flash(f"A list with id  {list_id} has been created successfully")
            return redirect(url_for("lister.shopping_list"))
        flash(
            f"A List with ID {list_id} already exists! You may use another ID or add new items to the existing one")
    else:
        flash("Both fields required: please try again")

    return render_template("shopping_list.html", shoppinglists=user.shopping_lists, user=user)


@lister.route("/edit/list/<list_id>", methods=["POST", "GET"])
def edit_list(list_id):
    """ edit_list defines routes for editing shopping lists with in the application"""
    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))

    user = app_instance.get_user(session["email"])
    shoppinglist = user.get_shoppinglist(list_id)
    if not shoppinglist:
        flash("That list doesn't exist")
        return redirect(url_for("lister.shopping_list"))

    if request.method == "POST":
        name = request.form["name"]
        notify_date = request.form["notify_date"]
        if not name or not notify_date:
            flash("Both fields required! Enter name and the notification date")
        else:
            if user.edit_shoppinglist(list_id, name, notify_date):
                flash(f"The list has been edited successfully")
                return redirect(url_for("lister.shopping_list"))
            flash("Unable to edit list")
    return render_template("edit_list.html", user=user, shoppinglist=shoppinglist)
