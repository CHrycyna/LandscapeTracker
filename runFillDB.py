from app import app, db
from app.models.user import User
from app.models.plant import Plant
from datetime import datetime, timedelta, date, time

u1 = User("Cam", "123")
db.session.add(u1)

p1 = Plant ("Feather Reed Grass", 
"Calamagrostis x acutiflora 'Karl Foerster'", 
"Perennial",
"3A",
"90",
"120",
"45",
"45")
db.session.add(p1)

p2 = Plant("Ivory Silk' Japanese Tree Lilac",
"Syringa reticulata 'Ivory Silk'",
"Tree",
"3A",
"20'",
"30'",
"15'",
"18'")
db.session.add(p2)

db.session.commit()

print("Successfully added entries to the Database.")