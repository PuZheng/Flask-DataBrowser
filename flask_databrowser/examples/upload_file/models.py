# -*- coding: UTF-8 -*-
from db import db


class File(db.Model):
    __tablename__ = "TB_FILE"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(32), nullable=False, unique=True)

    def __unicode__(self):
        return self.path

    def __repr__(self):
        return u"<User %s>" % self.path
