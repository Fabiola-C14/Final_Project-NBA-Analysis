# import necessary libraries
import os
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import update_data
from collections import namedtuple
from json import JSONEncoder
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# db_all = create_classes(db)
##############################################


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/api/predict")
def predict2020YIL5():
    # weather_facts = update_data.predict2020_YIL5()
    def movieJsonDecod(movieDict):
        return namedtuple('X', movieDict.keys())(*movieDict.values())

    with open('./static/datasets/top_2020_yil_5.json') as json_file:
        data = json.loads(json_file, object_hook=movieJsonDecod)
        
    return jsonify(data)

@app.route("/test")
def test():
    return render_template("test.html")





@app.route("/jane")
def jane():
    return render_template("jane.html")



@app.route("/naz")
def naz():
    return render_template("naz.html")



@app.route("/fabiola")
def fabiola():
    return render_template("fabiola.html")










































# NOT USING YET
# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():

    return render_template("")


@app.route("/api/pals")
def pals():

    return jsonify()







if __name__ == "__main__":
    app.run()
