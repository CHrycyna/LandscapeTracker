from test_helper import TestHelper

from app import app, db
from app.models.zone import Zone

class TestZone(TestHelper):
    def test_retrieve_zone(self):
        z = Zone("3A")
        assert z != None
