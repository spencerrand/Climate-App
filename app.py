# Import dependencies
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify

# Set up Flask
app = Flask(__name__)

# Create the connection engine to the sqlite database
engine = create_engine("sqlite:///data/hawaii.sqlite")

# Establish Base for which classes will be constructed 
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the stations class to a variable called `Station`
Station = Base.classes.stations

# Assign the measurements class to a variable called `Measurement`
Measurement = Base.classes.measurements

# To query the server we use a Session object
session = Session(bind=engine)

@app.route("/")
def home():
    return (
        f"<h1>Climate Analysis</h1><br/><br/>"
        f"Available Routes:<br/>"
        """<a href="/api/v1.0/stations">/api/v1.0/stations (List of stations)</a><br/>"""
        """<a href="/api/v1.0/tobs">/api/v1.0/tobs (Temperature observations for the previous year)</a><br/>"""
        """<a href="/api/v1.0/precipitation">/api/v1.0/precipitation (Precipitation for the previous year)</a><br/>"""
        """<a href="/api/v1.0/start-end">/api/v1.0/start-end (Temperature statistics for given ious year)</a><br/>"""
        "<form>"
            """Start Date: <input type="text" name="FirstName" value="Mickey"><br>"""
            """End Date: <input type="text" name="LastName" value="Mouse"><br>"""
        "</form>"
    )

@app.route("/api/v1.0/stations")
def stations():
    # Function returns a json list of stations from the dataset
    
    # Query database for stations
    stations = session.query(Station.station).all()
    
    # Convert object to a list
    station_list=[]
    for sublist in stations:
        for item in sublist:
            station_list.append(item)
    
    # Return jsonified list
    return (jsonify(station_list))

@app.route("/api/v1.0/tobs")
def tobs():
    # Function returns a json list of Temperature Observations (tobs) for the previous year
    
    # Calulate the date 1 year ago from today
    year_ago_dt = dt.date.today() - dt.timedelta(days=365)
    
    # Query database for stations
    tobs = session.query(Measurement.date, Measurement.tobs)\
            .filter(Measurement.date >= year_ago_dt)\
            .order_by(Measurement.date).all()
    
    # Convert object to a list
    tobs_list=[]
    for sublist in tobs:
        for item in sublist:
            tobs_list.append(item)
    
    # Return jsonified list
    return (jsonify(tobs_list))

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Function returns a json dictionary of dates and precipitation from the last year
    
    # Calulate the date 1 year ago from today
    year_ago_dt = dt.date.today() - dt.timedelta(days=365)
    
    # Query database for stations
    prcp = session.query(Measurement.date, Measurement.prcp)\
            .filter(Measurement.date >= year_ago_dt)\
            .order_by(Measurement.date).all()
    
    # Convert object to a list
    prcp_list=[]
    for sublist in prcp:
        for item in sublist:
            prcp_list.append(item)
    
    # Return jsonified list
    return (jsonify(prcp_list))

@app.route("/api/v1.0/<start>-<end>")
def temp_stats(start, end):
    # Function returns a json list of the minimum, average and maximum temperature for a given date range
    # Dates must be in YYYY-MM-DD format
       
    # Return jsonified list
    return ("Hi")

if __name__ == "__main__":
    app.run(debug=True)