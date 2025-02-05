# Import the dependencies.
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from flask import Flask, jsonify
from sql_helper import SQLHelper


DB_PATH = 'sqlite:///Resources/hawaii.sqlite'


# #################################################
# # Database Setup
# #################################################
# # Create engine using the `hawaii.sqlite` database file
# engine = create_engine(DB_PATH)
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# measurement = Base.classes.measurement
# station = Base.classes.station
# session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper(DB_PATH)
#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return """/api/v1.0/precipitation 
                /api/v1.0/stations
                /api/v1.0/tobs
                /api/v1.0/temp/<start>
                /api/v1.0/temp/<start>/<end>
            """ 

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Execute Query
    df = sqlHelper.queryPrecipitationSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    # Execute Query
    df = sqlHelper.queryStationsSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def temperature():
    # Execute Query
    df = sqlHelper.queryTempSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def tstats1(start):
    # Execute Query
    df = sqlHelper.queryTStatsSQL(start)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def tstats_se1(start, end):
    # Execute Query
    df = sqlHelper.queryTstats_SESQL(start, end)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)









