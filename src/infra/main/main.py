# -- coding: utf-8 --

from flask import Blueprint, render_template

#<--
package = "infra"
module = ""   

main = Blueprint("main", __name__, url_prefix="/" + module)

@main.route("/")
def index():
    return render_template("/infra/main/index.html")
    # return 'index'

@main.route("/test2")
def test2():
    return render_template("/infra/main/test2.html")
    # return 'index'

# @main.route("/login")
# def login():
#     return render_template("/infra/main/login.html")
    # return 'index'

# import sys
# print(sys.path)
