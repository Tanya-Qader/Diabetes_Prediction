import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///diabetes.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the tables.
Diabetes = Base.classes.diabetes

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
        f"<h1>Welcome to the Diabetes App API!</h1>"
        f"<h2>Here are the routes available:</h2>"
        f"Diabetes: /api/v1.0/diabetes<br/>"

@app.route('/api/v1.0/diabetes')
def precipitation():
    session = Session(engine)
    diabetes_selection = [Diabetes.ID, Diabetes.Diabetes, Diabetes.DifficultyWalking, Diabetes.HighBP, Diabetes.Income,
    Diabetes.HeartDisease, Diabetes.RaceEthnicity, Diabetes.OverallHealth, Diabetes.MentalHealth, Diabetes.Age, Diabetes.KidneyDisease, Diabetes.OverweightObese]
    query_result = session.query(*diabetes_selection).all()
    session.close()

    all_diabetes_info = []
    for ID,Diabetes,DifficultyWalking,HighBP,Income,HeartDisease,RaceEthnicity,OverallHealth,MentalHealth,Age,KidneyDisease,OverweightObese in query_result:
        diabetes_dict = {}
        diabetes_dict["ID"] = ID
        diabetes_dict["Diabetes"] = Diabetes
        diabetes_dict["DifficultyWalking"] = DifficultyWalking
        diabetes_dict["HighBP"] = HighBP
        diabetes_dict["Income"] = Income
        diabetes_dict["HeartDisease"] = HeartDisease
        diabetes_dict["RaceEthnicity"] = RaceEthnicity
        diabetes_dict["OverallHealth"] = OverallHealth
        diabetes_dict["MentalHealth"] = MentalHealth
        diabetes_dict["Age"] = Age
        diabetes_dict["KidneyDisease"] = KidneyDisease
        diabetes_dict["OverweightObese"] = OverweightObese

        all_diabetes_info.append(diabetes_dict)

    return jsonify(all_diabetes_info)


if __name__ == '__main__':
    app.run(debug=True)



    