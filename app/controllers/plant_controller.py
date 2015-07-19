 
from flask import render_template, flash, redirect, session, url_for, request, g, json, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from app.models import *
from app.models.plant import Plant
from sqlalchemy import or_
from datetime import datetime, time
import json

@app.route("/plants", methods=['GET'])
def get_plants():
    result = []
    
    plants = Plant.all()
    for plant in plants:
        result.append(plant.to_hash())

    w = {"Result":"OK", "Records": result}

    return jsonify(w)
