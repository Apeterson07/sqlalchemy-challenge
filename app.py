# Import the dependencies.
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify
from sql_helper import SQLHelper # isn't working/nothing wrong with flask

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine('hawaii.sqlite')

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the measurement class to a variable called `Measurement` and
#the station class to a variable called `Station`
measurement = Base.classes.measurement
station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()
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



