from flask import Blueprint, request, flash, redirect, render_template, url_for, session
from shoppinglister.models.user import User
from shoppinglister.models.shoppinglist import ShoppingList
from shoppinglister.models.item import Item
from shoppinglister.models.mainapp import App

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


@lister.route("/delete/list/<list_id>", methods=["GET", "POST"])
def delete_list(list_id):
    """delete_list defines routes for deleting a
    shopping list from a specified user account """
    error = None
    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))
    user = app_instance.get_user(session["email"])
    shoppinglist = user.get_shoppinglist(list_id)
    if not shoppinglist:
        return redirect(url_for("lister.shopping_list"))
    if request.method == "POST":
        if user.delete_shoppinglist(list_id):
            flash(f"List with {list_id} has been deleted successfully")
            return redirect(url_for("lister.delete_list", list_id=shoppinglist.list_id))
        error = f"Failed to delete {list_id}"
    return render_template("delete_list.html", error=error, shoppinglist=shoppinglist, user=user)


@lister.route("/view/list/items/<list_id>", methods=["POST", "GET"])
def items(list_id):
    """ Handles the display of all items with in a particular list"""
    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))
    user = app_instance.get_user(session["email"])
    shoppinglist = user.get_shoppinglist(
        list_id)  # returns a list of shop_items
    if not shoppinglist:
        return redirect(url_for("lister.shopping_list"))
    return render_template("items.html", user=user, shoppinglist=shoppinglist)


@lister.route("/add/list/item/<list_id>", methods=["POST"])
def add_item(list_id):
    """ defines routes for adding an item to a list"""
    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))
    user = app_instance.get_user(session["email"])
    shoppinglist = user.get_shoppinglist(list_id)

    name = request.form["name"]
    quantity = request.form["quantity"]
    price = request.form["price"]
    if not name or not quantity or not price:
        flash("All fields required: please recheck your inputs")
    else:

        item = Item(app_instance.generate_ID(), name, price, quantity)
        if shoppinglist.add_item(item):
            flash(f"{name} added successfully")
            return redirect(url_for("lister.items", list_id=list_id))
        flash(
            f"An item with name {name} already exists. Try editing it's price and quantity")
    return render_template("items.html", user=user, shoppinglist=shoppinglist)


@lister.route("/edit/list/item/<list_id>/<item_id>", methods=["GET", "POST"])
def edit_item(list_id, item_id):
    """ edit_item defines routes for editing an item within a list """

    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))
    user = app_instance.get_user(session["email"])
    shoppinglist = user.get_shoppinglist(list_id)
    item = shoppinglist.get_item(item_id)
    if not shoppinglist or not item:
        flash(f"Item doesn't exist on the mentioned shopping list")
        return redirect(url_for("lister.items", list_id=list_id))

    if request.method == "POST":
        name = request.form["name"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        if name and quantity and price:
            if shoppinglist.edit_item(item_id, name, quantity, price):
                flash(f"Item has successfully been edited")
                return redirect(url_for("lister.items", list_id=list_id))
            flash("Failed to edit item")
        else:
            flash("All inputs required, recheck your inputs and try again!")
    return render_template("edit_items.html", user=user, shoppinglist=shoppinglist, item=item)


@lister.route("/delete/list/item/<list_id>/<item_id>", methods=["GET", "POST"])
def delete_item(list_id, item_id):
    """ Defines routes for removing an item from a specified list """
    error = None

    if not session.get("logged_in"):
        flash("Please first login!")
        return redirect(url_for("lister.login"))

    user = app_instance.get_user(session["email"])
    shoppinglist = user.get_shoppinglist(list_id)
    item = shoppinglist.get_item(item_id)

    if not item or not shoppinglist:
        flash("Item doesn't exist on the shopping list with that name")
        return redirect(url_for("lister.items", list_id=list_id))

    if request.method == "POST":
        if shoppinglist.remove_item(item_id):
            flash("Item has successfully been deleted")
            return redirect(url_for("lister.items", list_id=shoppinglist.list_id))
        error = "Item has not been deleted"
    return render_template("delete_item.html", error=error, user=user, shoppinglist=shoppinglist, item=item)


@lister.route("/logout")
def logout():
    if session.get("logged_in"):
        session["logged_in"] = False
        del session["email"]
    return redirect(url_for("lister.signup"))
