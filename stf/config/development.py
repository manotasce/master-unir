import os

DEBUG=True
SECRET_KEY='development key!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data/data-dev.sqlite3')
FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
FLASKY_MAIL_SENDER = 'Administrador <manotasce.dev@gmail.com>'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL= False
MAIL_USERNAME='manotasce.dev@gmail.com'
MAIL_PASSWORD ='Sec.Account.001'
