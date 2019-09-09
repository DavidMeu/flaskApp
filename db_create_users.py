from app import db
from models import User

# insert data
db.session.add(User("David", "mdavid10@gmail.com", "i'll-never-tell"))
db.session.add(User("admin", "ad@min.com", "admin"))

# commit the changes
db.session.commit()
