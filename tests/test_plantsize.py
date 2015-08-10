from test_helper import TestHelper

from app import app, db
from app.models.plant_size import PlantSize

class TestPlantSize(TestHelper):

    def test_create_plant_size(self):
        ps1 = PlantSize(label='1 Gal')
        assert ps1 != None
        assert PlantSize.save_to_db(ps1) != False
        
    def test_validation(self):
        ps1 = PlantSize(label='1 Gal')
        PlantSize.save_to_db(ps1)
        ps2 = PlantSize(label='1 Gal')
        assert PlantSize.save_to_db(ps2) == False
    
    def test_tohash(self):
        ps1 = PlantSize(label='1 Gal')
        assert ps1.to_hash() == {'label': '1 Gal'}
        
    def test_tojson(self):
        ps1 = PlantSize(label='1 Gal')
        assert ps1.to_json() == '{"label": "1 Gal"}'