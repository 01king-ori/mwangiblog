import os

class Config:
    SECRET_KEY = '123098'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vincent:1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kingorimwangi01@gmail.com'
    MAIL_PASSWORD = 'xpsviewer2001'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vincent:1234@localhost/blog'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}