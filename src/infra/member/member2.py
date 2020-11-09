# -- coding: utf-8 --
from flask import Blueprint

module = "member"   

member = Blueprint("member", __name__, url_prefix="/" + module )

moduleObj = member

@moduleObj.route('/list')
def list():
    return 'member list'

@moduleObj.route('/view')
def view():
    return 'member view'