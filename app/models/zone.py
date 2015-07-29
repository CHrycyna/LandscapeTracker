from app import db
from sqlalchemy.sql import *
from sqlalchemy.ext.hybrid import hybrid_property
import json
from datetime import datetime, date
from app.utility import is_blank

class Zone(db.Model):
    __tablename__ = 'zone'
    id = db.Column(db.Integer, primary_key=True)
    zone = db.Column(db.String, nullable=False)
    
    def __init__(self, zone=None):
        self.zone = zone
        
    def __passes_validations(zone):
        return( (not is_blank(zone)) and (Zone.query.filter(Zone.zone == zone).first()) )
    
    @staticmethod
    def save_to_db(zone):
     if zone != None:
       if zone.id == None:            
           if Zone.__passes_validations(zone):
               db.session.add(zone)
               db.session.commit()
               return True
           return False
       db.session.add(zone)
       db.session.commit()
       return True
    