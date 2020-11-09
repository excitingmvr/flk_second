# -- coding: utf-8 --

from flask import Flask, Blueprint
import sys

from src.common.constants import Constants as constantsObj

sys.path.append(constantsObj.SOURCE_PAHT_WINDOWS)

app = Flask(__name__)

from src.infra.main.main import main
from src.infra.member.member import member

app.register_blueprint(main)
app.register_blueprint(member)


# filter
from  src.common.filter import *
 
app.jinja_env.filters['seqEncode'] = seqEncode
app.jinja_env.filters['seqDecode'] = seqDecode
# app.jinja_env.filters['convertDateYear'] = convertDateYear
# app.jinja_env.filters['convertDateMonth'] = convertDateMonth
# app.jinja_env.filters['convertDateDay'] = convertDateDay

app.jinja_env.filters['nl2br'] = nl2br

app.jinja_env.filters['setReduceString'] = setReduceString
app.jinja_env.filters['bytesToMega'] = bytesToMega

app.jinja_env.filters['displayGender'] = displayGender
app.jinja_env.filters['displayNy'] = displayNy
app.jinja_env.filters['displayDevice'] = displayDevice