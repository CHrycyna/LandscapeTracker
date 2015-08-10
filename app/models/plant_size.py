from app import db
from sqlalchemy.sql import *
from sqlalchemy.ext.hybrid import hybrid_property
import json
from datetime import datetime, date
from app.utility import is_blank

class PlantSize(db.Model):
    __tablename__ = 'plant_size'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)

    def __init__(self,
    label=None):
        self.label = label

    def to_json(self):
        return json.dumps(self.to_hash())
    
    def to_hash(self):
        ret = { "label": self.label }
        return ret
        
    @staticmethod
    def find_by_label(label):
        return (PlantSize.query.filter(PlantSize.label == label).first())
        
    @staticmethod
    def save_to_db(label):
     if label != None:
       if label.id == None:            
           if PlantSize.__passes_validations(label):
               db.session.add(label)
               db.session.commit()
               return True
           return False
       db.session.add(label)
       db.session.commit()
       return True
    
    @staticmethod
    def __passes_validations(size):
        return( (not is_blank(size.label)) and (not is_blank(size.label)) and (PlantSize.find_by_label(size.label) == None) )
        
    @staticmethod
    def all():
        return (Plant.query.all())