# Imports
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Setup the app instance
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Setup the DB according to the ORM
db = SQLAlchemy(app)

# Import + Register Blueprint(s)
# You can have several Blueprints, although
# we only have one in this backend for the sake of example
