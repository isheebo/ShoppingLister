import os
from flask import Flask
from shoppinglister.views import lister

app = Flask(__name__)
app.register_blueprint(lister)
app.secret_key = os.urandom(64)
