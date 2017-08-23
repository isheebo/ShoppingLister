import os
from flask import Flask
from models.views import lister

app = Flask(__name__)
app.register_blueprint(lister)
app.secret_key = os.urandom(64)

if __name__ == '__main__':
    app.run(debug=True)
