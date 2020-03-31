# Importing Dependencies
import numpy as np
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta


# Database prep
import sqlalchemy as db
from sqlalchemy import desc
engine = db.create_engine('sqlite:///Resources/hawaii.sqlite')
connection = engine.connect()
metadata = db.MetaData()



# Flask Setup
from flask import Flask, jsonify
app = Flask(__name__)


# Routes

# List all routes
@app.route("/")
def welcome():
    return (
         f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    year_ago = date(2017, 8, 23) - timedelta(days = 365)

    query = db.select([M.columns.date, M.columns.prcp]).where(M.columns.date >= year_ago)
    precip_data = connection.execute(query).fetchall()

    precip = {date: prcp for date, prcp in precip_data}
    return jsonify(precip)
