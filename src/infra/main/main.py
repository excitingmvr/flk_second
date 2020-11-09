# -- coding: utf-8 --

from flask import Blueprint, render_template

module = ""
main = Blueprint("main", __name__, url_prefix="/" + module)

@main.route("/")
def index():
    return render_template("/main/index.html")
    # return 'index'

@main.route("/test2")
def test2():
    return render_template("/main/test2.html")
    # return 'index'


# import sys
# print(sys.path)
