import os

DEBUG=True
SECRET_KEY='development key!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data/data-dev.sqlite3')