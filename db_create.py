from project import db
#from project.models import BlogPost

#create the database and the db tables
#creating the db based on the models.py file
db.create_all()


#insert
#db.session.add(BlogPost("Good", "I\'m good."))
#db.session.add(BlogPost("Well", "I\'m well."))
#db.session.add(BlogPost("Flask", "discoverflask.com"))
#db.session.add(BlogPost("postgres", "we setup a local postgres instance"))
#commit the changes
db.session.commit()
