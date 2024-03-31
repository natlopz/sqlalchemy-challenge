# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta

app = Flask(__name__)

#################################################
# Database Setup
#################################################
# create a reference to the file
database_path = pathlib.Path('C:/Users/lnata/Github/sqlalchemy-challenge/Resources/hawaii.sqlite')

# create engine to hawaii.sqlite
engine = create_engine(f"sqlite:///{database_path}")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=False)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"  
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

#################################################
# Flask Routes
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date 1 year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    precipitation_data = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= one_year_ago)\
        .all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitations.
    all_precipitations = {date: prcp for date, prcp in precipitation_data}

    # Return the JSON representation of your dictionary.
    return jsonify(all_precipitations)

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations.
    stations = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list.
    all_stations = list(np.ravel(stations))

    # Return a JSON list of stations from the dataset.
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date 1 year ago from the last data point in the database.
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the dates and temperature observations of the most-active station for the previous year of data.
    results = session.query(Measurement.tobs)\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date >= one_year_ago)\
        .all()

    session.close()

    # Convert list of tuples into normal list.
    tobs_list = list(np.ravel(results))

    # Return a JSON list of temperature observations for the previous year.
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):
    from datetime import datetime, timedelta
    # Find the most recent date in the data set.
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date

    recent_date_str = recent_date[0]

    # Convert the string to a datetime object.
    recent_date_obj = datetime.strptime(recent_date_str, '%Y-%m-%d')

    # Calculate the start date by subtracting one year (365 days) from the most recent date.
    start_date_obj = recent_date_obj - timedelta(days=365)

    # Convert the start date back to a string .
    start_date_str = start_date_obj.strftime('%Y-%m-%d')

    results = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs), 
                            func.max(Measurement.tobs))\
                      .filter(Measurement.date >= start_date_str).all()
    
    session.close()

     # Unpack the result and prepare the JSON response
    TMIN, TAVG, TMAX = results[0]
    temp_stats = {
        "TMIN": TMIN,
        "TAVG": TAVG,
        "TMAX": TMAX
    }

    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Find the most recent date in the data set.
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date

    recent_date_str = recent_date[0]

    # Convert the string to a datetime object.
    recent_date_obj = datetime.strptime(recent_date_str, '%Y-%m-%d')

    # Calculate the start date by subtracting one year (365 days) from the most recent date.
    start_date_obj = recent_date_obj - timedelta(days=365)

    # Convert the start date back to a string .
    start_date_str = start_date_obj.strftime('%Y-%m-%d')

    # Query for the min, avg, and max temperatures between the start and end dates
    results = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs), 
                            func.max(Measurement.tobs))\
                      .filter(Measurement.date >= start_date_str, Measurement.date <= recent_date_str).all()

    session.close()

    # Unpack the result and prepare the JSON response
    TMIN, TAVG, TMAX = results[0]
    temp_stats = {
        "TMIN": TMIN,
        "TAVG": TAVG,
        "TMAX": TMAX
    }

    return jsonify(temp_stats)   

if __name__ == '__main__':
    app.run(debug=True)