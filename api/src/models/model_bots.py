import sys
import os
basedir = os.path.abspath(os.path.dirname("../"))
sys.path.insert(0, basedir)
from src import db


class Bots(db.Model):

    __tablename__ = 'bots'

    id = db.Column(db.Integer(), primary_key=True)
    comment = db.Column(db.String())
    login = db.Column(db.String())
    password = db.Column(db.String())
    steam_id = db.Column(db.String())
    shared_secret = db.Column(db.String())
    identity_secret = db.Column(db.String())
    steam_api = db.Column(db.String())
    tm_api = db.Column(db.String())
    google_drive = db.Column(db.String())
    proxy = db.Column(db.String())
    is_active = db.Column(db.Boolean(), default=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'comment': self.comment,
            # This is an example how to deal with Many2Many relations
            'login': self.login
        }
    # categ3 = db.Column(db.String())



