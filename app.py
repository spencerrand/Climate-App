# Import dependencies
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
from flask import Flask, jsonify

app = Flask(__name__)

# Create the connection engine to the sqlite database
engine = create_engine("sqlite:///data/hawaii.sqlite")

# Establish Base for which classes will be constructed 
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the demographics class to a variable called `Demographics`
Station = Base.classes.stations

# Assign the demographics class to a variable called `Demographics`
Measurement = Base.classes.measurements

# To push the objects made and query the server we use a Session object
session = Session(bind=engine)

@app.route("/")
def home():
    return (
        f"<h1>Climate Analysis</h1><br/><br/>"
        f"Available Routes:<br/>"
        """<a href="/api/v1.0/stations">Click here to see the list of stations</a><br/>"""
    )

@app.route("/api/v1.0/stations")
def stations():
    
    stations = session.query(Station.station, Station.name).all()
    return (jsonify(dict(stations)))

if __name__ == "__main__":
    app.run(debug=True)