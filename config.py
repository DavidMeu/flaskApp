import os

# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xa9\xde\xfd\x95\xe8L\x08g)F\xf0\xf8\x1e\xa1\xe9kx\x0e!\x89\x9d\x16\xb5\xfa'
	# export DATABASE_URL="sqlite:///posts.db"
	# export DATABASE_URL="postgresql:///discover_flask_dev"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	print(SQLALCHEMY_DATABASE_URI)
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False