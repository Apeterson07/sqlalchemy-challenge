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


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper(DB_PATH)

#################################################
# Flask HTML Routes
#################################################
@app.route("/")
def home():
    return """/api/v1.0/precipitation<br>
                /api/v1.0/stations<br>
                /api/v1.0/tobs<br>
                /api/v1.0/temp/&lt;start&gt;<br>
                /api/v1.0/temp/&lt;start&gt;/&lt;end&gt;<br>
            """ 


#################################################
# Flask API Routes
#################################################
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
    df = sqlHelper.queryTemperatureSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/temp/<start>/")
def tstats1(start):
    # Execute Query
    df = sqlHelper.queryTStatsSQL(start)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/temp/<start>/<end>/")
def tstats_se1(start, end):
    # Execute Query
    df = sqlHelper.queryTStats_StartEndSQL(start, end)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)


#################################################
# Run Flask APP/Server
#################################################
if __name__ == '__main__':
    app.run(debug=True)









