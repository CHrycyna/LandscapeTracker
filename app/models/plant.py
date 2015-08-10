from app import db
from sqlalchemy.sql import *
from sqlalchemy.ext.hybrid import hybrid_property
import json
from datetime import datetime, date
from app.utility import is_blank

class Plant(db.Model):
    __tablename__ = 'plant'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, nullable=False)
    plant_id = db.Column(db.Integer, nullable=False)
    name_common = db.Column(db.String, nullable=False)
    name_botanical = db.Column(db.String, nullable=False)
    plant_type = db.Column(db.String, nullable=True)
    zone = db.Column(db.String, nullable=True)
    
    plant_height_min = db.Column(db.Integer, nullable=True)
    plant_height_max = db.Column(db.Integer, nullable=True)
     
    plant_width_min = db.Column(db.Integer, nullable=True)
    plant_width_max = db.Column(db.Integer, nullable=True)
    
    added_at = db.Column(db.DateTime, nullable=False)
    edited_at = db.Column(db.DateTime, nullable=False)


    def __init__(self,
    group_id=None,
    plant_id=None,
    name_common=None, 
    name_botanical=None, 
    plant_type=None, 
    zone=None, 
    plant_height_min=None, 
    plant_height_max=None, 
    plant_width_min=None, 
    plant_width_max=None):
        self.group_id = group_id
        self.plant_id = plant_id
        self.name_common = name_common
        self.name_botanical = name_botanical
        self.plant_type = plant_type
        self.zone = zone
        self.plant_height_min = plant_height_min
        self.plant_height_max = plant_height_max
        self.plant_width_min = plant_height_max
        self.plant_width_max = plant_width_max
        self.added_at = datetime.now() 
        self.edited_at = datetime.now()
        
    def to_json(self):
        return json.dumps(self.to_hash())
    
    def to_hash(self):
        format = '%Y-%m-%d %H:%M'
        ret = { "name_common": self.name_common ,
                "name_botanical": self.name_botanical,
                "plant_type": self.plant_type,
                "zone": self.zone,
                "plant_height_min": self.plant_height_min,
                "plant_height_max": self.plant_height_max,
                "plant_width_min": self.plant_width_min,
                "plant_width_max": self.plant_width_max,
                "added_at": self.added_at.strftime(format),
                "edited_at": self.edited_at.strftime(format) }
        return ret
        
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
        return( (not is_blank(plant.name_common)) and (not is_blank(plant.name_botanical)) and (Plant.find_by_botanical(plant.name_botanical) == None) )
        
    @staticmethod
    def all():
        return (Plant.query.all())