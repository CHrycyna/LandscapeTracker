from test_helper import TestHelper

from app import app, db
from app.models.plant import Plant

class TestPlant(TestHelper):

    def test_create_plant(self):
        p = Plant(name_common='Feather Reed Grass', name_botanical="other")
        assert Plant.save_to_db(p) == True
        plant = Plant.find_by_botanical("other")
        assert plant != None
        
    def test_validation(self):
        p1 = Plant(name_common='Feather Reed Grass', name_botanical="other")
        Plant.save_to_db(p1)
        p2 = Plant(name_common='Feather Reed Grass', name_botanical="other")
        assert Plant.save_to_db(p2) == False