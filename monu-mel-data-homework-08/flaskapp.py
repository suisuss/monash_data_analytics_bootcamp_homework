import datetime as dt
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Database
engine = create_engine('sqlite:///./Resources/hawaii.sqlite')

# Reflect existing database
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Viewing all the classes
Base.classes.keys()

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station


@app.route("/")
def index():
    return jsonify({"message": "Welcome! Go to /api/v1.0/precipitation for preciptation data. Go to /api/v1.0/stations for station data. Go to /api/v1.0/tobs for tobs data. Go to /api/v1.0/temperature for temperature data."})

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create database session
    session = Session(engine)

    # Extract data
    selection = [measurement.date, measurement.prcp]
    data = session.query(*selection).all()

    # Close the session
    session.close()

    # Put data in a dictionarie
    precipitation_dict = {}
    for date, precipitation in data:
        precipitation_dict[date] = precipitation

    if len(precipitation_dict) < 1:
        return jsonify({"error": "Data not found"}), 404

    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Create database session
    session = Session(engine)
    # Extract data
    data = session.query(measurement.station).distinct().all()
    # Close the session
    session.close()
    # Put data into a list of dicts
    stations_list= [{"station": row[0]} for row in data]

    if len(stations_list) < 1:
        return jsonify({"error": "Data not found"}), 404

    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create database session
    session = Session(engine)
    # Extract Data
    last_date = session.query(func.max(measurement.date))
    last_date = last_date[0][0]
    # One year ago calculation
    one_year_ago = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Most active station for the last year of data
    query = ["Select station, count(station) \
                From Measurement Group By station \
                Order By count(station) Desc"]
    most_active_station = engine.execute(*query).fetchone()
    select_station = most_active_station[0]

    data = session.query(measurement.date, measurement.tobs).\
                        filter(measurement.date >= one_year_ago.strftime("%Y-%m-%d")).\
                        filter(measurement.date <= last_date).\
                        filter(measurement.station == select_station).all()

    # Close the session
    session.close()

    # Put data into a list of dicts
    temperature_list= [{"date": row[0], "temperature": row[1]} for row in data]

    if len(temperature_list) < 1:
        return jsonify({"error": "Data not found"}), 404
    
    return jsonify(temperature_list)

@app.route("/api/v1.0/temperature", methods=['GET'])
def temperature():
    param = request.args.to_dict()
    # Verify that there are parameters
    if len(param) < 1:
        return jsonify({"error": "Data not found. Parameters 'start' and/or 'end' date must be provided."}), 404

    # Create database session
    session = Session(engine)

    if param.get('start'):
        data = session.query(measurement.date, func.min(measurement.tobs),\
                        func.round(func.avg(measurement.tobs),1),\
                        func.max(measurement.tobs)).\
                        filter(measurement.date >= param['start']).\
                        group_by(measurement.date).all()

    if param.get('start') and param.get('end'):
        data = session.query(measurement.date, func.min(measurement.tobs),\
                        func.round(func.avg(measurement.tobs),1),\
                        func.max(measurement.tobs)).\
                        filter(measurement.date >= param['start']).\
                        filter(measurement.date <= param['end']).\
                        group_by(measurement.date).all()

    # Close the session
    session.close()

    # Put data into a list of dicts
    temperature_list= [{"date": row[0], "min": row[1], "max": row[3], "average": row[2]} for row in data]

    if len(temperature_list) < 1:
        return jsonify({"error": "Data not found"}), 404
    
    return jsonify(temperature_list), 200

if __name__ == '__main__':
    app.run(debug=True)