# import necessary libraries
import numpy as np
import pandas as pd 

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask_sqlalchemy import sqlalchemy

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

#####################The following code will allow you to inspect the DB to see what tables and columns are there using reflection
# Create the connection engine
engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")

# Create the inspector and connect it to the engine
### BEGIN SOLUTION
#inspector = inspect(engine)
### END SOLUTION

# Collect the names of tables within the database
### BEGIN SOLUTION
#inspector.get_table_names()
### END SOLUTION

# Using the inspector to print the column names within the 'Salaries' table and its types
### BEGIN SOLUTION
# columns = inspector.get_columns('Salaries')
# for column in columns:
#     print(column["name"], column["type"])
### END SOLUTION



#####################The code below allow you to map classes from the DB using reflection

# Declare a Base using `automap_base()`
### BEGIN SOLUTION
Base = automap_base()
### END SOLUTION

# Use the Base class to reflect the database tables
### BEGIN SOLUTION
Base.prepare(engine, reflect=True)
### END SOLUTION

# Print all of the classes mapped to the Base
### BEGIN SOLUTION
Base.classes.keys()
### END SOLUTION

# Assign the demographics class to a variable called `Demographics`
### BEGIN SOLUTION
Otu = Base.classes.otu
Samples = Base.classes.samples 
Samples_Metadata = Base.classes.samples_metadata 

### END SOLUTION

# Create a session
### BEGIN SOLUTION
session = Session(engine)
### END SOLUTION


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/names")
def names():
    bbb_samples = "/db/belly_button_biodiversity_samples.csv"
    bbb_samples_df = pd.read_csv(bbb_samples, encoding = "utf-8")
    # grab the headers into a list
    sample_names =  list(bbb_samples_df)
    # get rid of the 1st header
    del sample_names[0]
    return jsonify(sample_names)


# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         pet_type = request.form["petType"]
#         age = request.form["petAge"]

#         pet = Pet(name=name, type=pet_type, age=age)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("http://localhost:5000/", code=302)

#     return render_template("form.html")


# @app.route("/api/names")
# def names():
#     import pandas as pd 
#     import csv
#     import os
#     csvpath = os.path.join('db', 'belly_button_biodiversity_samples.csv')

#     with open(csvpath, newline='') as samplefile:

# # CSV reader specifies delimiter and variable that holds contents
#         samplereader = csv.reader(samplefile, delimiter=',')
#         sample_df = pd.DataFrame(samplereader)
#         sampleResults = sample_df.columns.values.tolist()

# #  Each row is read as a row
#         #for row in samplereader:
#         return jsonify(sampleResults)

    
    
    #return jsonify(sampleResults)

# @app.route("/api/pals")
# def pals():
#     results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()

#     pet_type = [result[0] for result in results]
#     age = [result[1] for result in results]

#     pet_data = {
#         "x": pet_type,
#         "y": age,
#         "type": "bar"
#     }

#     return jsonify(pet_data)

# @app.route("/api/names")
# def pets():
#     results = db.session.query(Pet.name).all()
#     print(results)
#     all_pets = list(np.ravel(results))
#     return jsonify(all_pets)

if __name__ == "__main__":
    app.run()
