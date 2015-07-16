from app import db
from sqlalchemy.sql import *
from sqlalchemy.ext.hybrid import hybrid_property
import json
from datetime import datetime, date
from app.utility import is_blank

class Plant(db.Model):
    __tablename__ = 'plant'
    id = db.Column(db.Integer, primary_key=True)
    name_commom = db.Column(db.String, nullable=False)
    name_botanical = db.Column(db.String, nullable=False)
    plant_type = db.Column(db.String, nullable=True)
    plant_height = db.Column(db.Integer, nullable=True)
    plant_width = db.Column(db.Integer, nullable=True)
    added_at = db.Column(db.DateTime, nullable=False)
    edited_at = db.Column(db.DateTime, nullable=False)


    def __init__(self, name_commom=None, name_botanical=None):
        self.name_commom = name_commom
        self.name_botanical = name_botanical
        self.added_at = datetime.now() 
        self.edited_at = datetime.now()
    
    @staticmethod
    def find_by_botanical(name_botanical):
        return (Plant.query.filter(Plant.name_botanical == name_botanical).first())
        
    @staticmethod
    def save_to_db(plant):
     if plant != None:
       if plant.id == None:            
           if Plant.__passes_validations(plant):
               db.session.add(plant)
               db.session.commit()
               return True
           return False
       db.session.add(plant)
       db.session.commit()
       return True
    
    @staticmethod
    def __passes_validations(plant):
        return( (not is_blank(plant.name_commom)) and (not is_blank(plant.name_botanical)) and (Plant.find_by_botanical(plant.name_botanical) == None) )