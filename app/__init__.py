from flask import Flask
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from app import routes


app.run(host="0.0.0.0", debug=True)