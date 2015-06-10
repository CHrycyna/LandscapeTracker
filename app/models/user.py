from app import db
from sqlalchemy.sql import *
from sqlalchemy.ext.hybrid import hybrid_property
import json
from datetime import datetime, date
from hashlib import md5
from app.utility import is_blank

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index = True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, index = True, unique=True)
    firstname = db.Column(db.String, nullable=True)
    lastname = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    sex = db.Column(db.String(1), nullable=True)
    date_of_birth = db.Column(db.String, nullable=True)
    avatar = db.Column(db.String, nullable=True)
    about_me = db.Column(db.String(140), nullable=True)
    last_seen = db.Column(db.DateTime, nullable=True)
    registered_at = db.Column(db.DateTime, nullable=False)


    def __init__(self, username=None, password = None, email=None, firstname=None, lastname=None,
                location=None, sex=None, date_of_birth=None, avatar=None, about_me=None, last_seen=None):
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.avatar = avatar
        self.about_me = about_me
        self.last_seen = last_seen
        self.registered_at = datetime.now() 

    def to_json(self):
        ret = { "username": self.username, "email": self.email, "gender": self.sex, "age": self.get_user_age(), "birth": self.date_of_birth, "gravatar": self.avatar,
            "firstname": self.firstname, "lastname": self.lastname, "location": self.location, "avatar":self.get_avatar(400), "about_me":self.about_me,
            "sex": self.sex, "id": self.id, "registration_date":self.registered_at.strftime('%B %d, %y')}
        return json.dumps(ret)
    
    def to_hash(self):
        format = '%d-%m-%Y / %H:%M'
        ret = { "username": self.username, "email": self.email,
                "firstname": self.firstname, "lastname": self.lastname, "location": self.location,
                "avatar": self.avatar, "sex": self.sex, "id": self.id, "date":self.registered_at.strftime(format)}
        return ret
    
    @staticmethod
    def getNewest():
        return User.query.order_by(desc(User.registered_at)).first()

    @hybrid_property
    def first_last_name(self):
        return self.firstname + " " + self.lastname

    @hybrid_property
    def last_first_name(self):
        return self.lastname + " " + self.firstname
    
    @staticmethod
    def find_by_id(id):
        return (User.query.filter(User.id == id).first())

    @staticmethod
    def find_by_username(username):
        return (User.query.filter(User.username == username).first())

    @staticmethod
    def find_all_by_username(username):
        return User.query.filter(User.username.like('%' + username + '%')).all()

    @staticmethod
    def find_by_email(email):
        return (User.query.filter(User.email == email).first())

    @staticmethod
    def find_all_by_email(email):
        return User.query.filter(User.email.like('%' + email + '%')).all()

    @staticmethod
    def all():
        return (User.query.all())

    @staticmethod
    def save_to_db(user):
     if user != None:
       if user.id == None:            
           if User.__passes_validations(user):
               db.session.add(user)
               db.session.commit()
               return True
           return False
       db.session.add(user)
       db.session.commit()
       return True
   	
    @staticmethod
    def __passes_validations(user):
        return( (not is_blank(user.username)) and (not is_blank(user.password))
   	    and (User.find_by_username(user.username) == None) )
   
    def update_profile(self):
        return True

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user) and self.id != user.id:
            self.followed.remove(user)
            return self
        
    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def user_is_following(self):
        return User.query.join(followers, (followers.c.followed_id == User.id)).filter(followers.c.follower_id == self.id).order_by(User.username).group_by(User.username)
      
    def followed_posts(self):
        return Newsfeed.query.join(followers, (followers.c.followed_id == Newsfeed.user_id)).filter(followers.c.follower_id == self.id).order_by(Newsfeed.timestamp.desc())
    
    def top_user(self):
        return self.followed.group_by(followers.c.followed_id).order_by(desc(func.count(followers.c.followed_id))).limit(1).all()
 
    def valid_password(self, password_to_validate):
        return self.password == password_to_validate

    def __repr__(self):
        return "%s" % (self.username)

