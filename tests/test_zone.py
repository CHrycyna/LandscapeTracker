from test_helper import TestHelper

from app import app, db
from app.models.zone import Zone

class TestZone(TestHelper):
    def test_add_zone(self):
        z = Zone("3A")
        assert z != None
        assert Zone.save_to_db(z) == True
        
    def test_add_duplicate_zone(self):
        z = Zone("3A")
        z2 = Zone("3A")
        Zone.save_to_db(z)
        assert Zone.save_to_db(z2) == False
        
        
