import os
import env
from db import db

from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_restful import Api

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['DEBUG'] = True
api = Api(app)

Bootstrap(app)

# DATASETS & MODELS
import json
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
dataset_json = os.path.join(my_path, "../../static/datasets/dataset.json")


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    dataset = json.load(open("dataset.json"))
    return render_template("dashboard.html", dataset=dataset['data'])


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## DB INIT
db.init_app(app)

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()
