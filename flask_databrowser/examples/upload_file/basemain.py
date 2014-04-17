
# -*- coding: UTF-8 -*-
"""
SYNOPSIS
    python basemain.py [options]
OPTIONS
    -h
        show this help
    -p  <port>
        the port of server runs on
    -s  <host>
        the ip of the server runs on
"""
import sys
from getopt import getopt
from flask import Flask, Blueprint, redirect
from flask.ext import databrowser
from flask.ext import upload2

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp.db"
app.config['SQLALCHEMY_ECHO'] = False
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "JHdkj1;"
app.config["CSRF_ENABLED"] = False

from flask.ext.babel import Babel
Babel(app)
upload2.FlaskUpload(app)

class FileModelView(databrowser.ModelView):

    can_create = True
    create_template = edit_template = 'file/form.html'

    @property
    def create_columns(self):
        return [
            databrowser.col_spec.FileColSpec('path')
        ]


files_bp = Blueprint("files", __name__, static_folder="static",
                     template_folder="templates")


@app.route("/")
def index():
    return redirect(file_model_view.url_for_list())

if __name__ == "__main__":

    opts, _ = getopt(sys.argv[1:], "hp:s:")
    for o, v in opts:
        if o == '-h':
            print __doc__
            sys.exit(0)
        elif o == '-p':
            port = v
        elif o == '-s':
            host = v
        else:
            print 'unkown option: ' + v
            print __doc__
            sys.exit(-1)

    try:
        port
    except NameError:
        port = 5000

    try:
        host
    except NameError:
        host = '0.0.0.0'

    from models import File
    from db import db

    data_browser = databrowser.DataBrowser(app)
    file_model_view = FileModelView(databrowser.sa.SAModell(File, db, u"文件"),
                                    permission_required=False)
    data_browser.register_model_view(file_model_view, files_bp)

    app.register_blueprint(files_bp, url_prefix="/files")
    app.run(port=port, host=host)
