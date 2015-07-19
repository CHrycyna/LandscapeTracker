
from flask import render_template, flash, redirect, session, url_for, request, g, json, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from app.models import *
from app.models.user import User
from sqlalchemy import or_
from datetime import datetime, time
import json
#from config import MAX_SEARCH_RESULTS, POSTS_PER_PAGE

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

@app.route("/")
def home_index():
    print "Here"
    return render_template("index.html")

#ErrorHandlers
#
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
