from test_helper import TestHelper

from app import app, db
from app.models.user import User

class TestUser(TestHelper):

    def test_retrieve_user(self):
        u = User(username = 'andy', password = "123", email = 'umluo23@cc.umanitoba.ca')
        db.session.add(u)
        db.session.commit()
        user = User.find_by_username('andy')
        assert user.username == 'andy'

    def test_find_by_id(self):
        u = User(username = 'jack_nicholson', password = "123", email =
                'j@example.com')
        User.save_to_db(u)
        user = User.find_by_id(1)
        assert user != None

    def test_find_all(self):
        u = User(username = 'jack_nicholson', password = "123", email =
                'j2@example.com')
        User.save_to_db(u)
        u = User(username = 'random_person', password = "123", email =
                'j3@example.com')
        User.save_to_db(u)
        u = User(username = 'jason_spezza', password = "123", email =
                'j1@example.com')
        User.save_to_db(u)

        assert len(User.all()) == 3

    def test_inserting_duplicate_username(self):
        u = User(username = 'jack_nicholson', password = "123", email =
                'j2@example.com')
        User.save_to_db(u);
        u2 = User(username = 'jack_nicholson', password = "123", email =
                'j33@example.com')

        assert User.save_to_db(u2) == False
        assert len(User.all()) == 1

    def test_empty_username(self):
        u = User(username = '', password = "123", email =
                'j2@example.com')
        assert User.save_to_db(u) == False
        assert len(User.all()) == 0

    def test_empty_password(self):
        u = User(username = 'jason_spezza', password = "", email =
                'j1@example.com')
        assert User.save_to_db(u) == False
        assert len(User.all()) == 0
        