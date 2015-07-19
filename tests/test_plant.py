from test_helper import TestHelper

from app import app, db
from app.models.plant import Plant

class TestPlant(TestHelper):

    def test_create_plant(self):
        p = Plant(name_commom='Feather Reed Grass', name_botanical="other")
        Plant.save_to_db(p)
        plant = Plant.find_by_botanical("other")
        assert plant != None