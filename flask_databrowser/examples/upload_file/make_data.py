#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import types

from db import db
from models import File
db.create_all()


def do_commit(obj, action="add"):
    if action == "add":
        if isinstance(obj, types.ListType) or isinstance(obj, types.TupleType):
            db.session.add_all(obj)
        else:
            db.session.add(obj)
    elif action == "delete":
        db.session.delete(obj)
    db.session.commit()
    return obj

do_commit(File(path="abc.txt"))
