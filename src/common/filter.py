# -- coding: utf-8 --

import base64, hashlib

from src.common.constants import Constants

constantsObj = Constants()

def seqEncode(rt):
    tmp = str(rt) + constantsObj.HASH_SUFFIX
    rtEncoded = base64.urlsafe_b64encode(bytes(tmp, 'UTF-8')).decode("UTF-8").rstrip("=") 
    # print('rtEncoded:', rtEncoded)
    return rtEncoded


def seqDecode(rt):
    rt = str(rt)
    rt = rt + ("=" * (4 - (len(rt) % 4)))
    rtDecoded = base64.urlsafe_b64decode(bytes(rt, 'UTF-8'))[:-4]
    return int(rtDecoded)


def setReduceString(param, num):
    return param[:num] + "..."


def bytesToMega(num):
    return round((num / 1048576), 2)


def displayGender(param):
    if param == 1:
        result = "Male"
    elif param == 2:
        result = "Female"
    elif param == 3:
        result = "Etc"
    else:
        result = "NA"
    return result


def displayNy(param):
    if param == 0:
        result = "N"
    else:
        result = "Y"
    return result


def displayDevice(param):
    if param == 1:
        result = "PC"
    elif param == 2:
        result = "Mobile"
    elif param == 3:
        result = "Tablet"
    elif param == 4:
        result = "Etc"
    else:
        result = "NA"
    return result


def getYearInt(param):
    result = int(param.strftime('%Y'))
    return result


def getMonthInt(param):
    result = int(param.strftime('%m'))
    return result


def getDayInt(param):
    result = int(param.strftime('%d'))
    return result


def hashPwdUser(pwd, kind):
    if kind == 1:       # sha256
        result = hashlib.sha256(pwd.encode()).hexdigest()
    return result


# nl2br start
import re
from jinja2 import evalcontextfilter, Markup, escape

_paragraph_re = re.compile(r'(?:\r\n|\r(?!\n)|\n){2,}')

@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', Markup('<br>\n'))
                          for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
# nl2br end

## old version ##################################################

# def seqEncode(rt):
#     tmp = str(rt) + constantsObj.HASH_SUFFIX
#     rtEncoded = base64.b64encode(tmp.encode()).decode('UTF-8')
#     return rtEncoded

# def convertDateYear(value):
#     if value != None:
#         return value.strftime('%Y')

# def convertDateMonth(value):
#     return value.strftime('%m')

# def convertDateDay(value):
#     return value.strftime('%d')

# def setDateYear(rt){

    
# }
# def seqEncode(rt):
#     return hashlib.md5(str(rt).encode()).hexdigest()

# def seqDecode(rt):
#     for i in range(123):
#         rtDecoded = str(rt).replace(hashlib.md5(chr(i).encode()).hexdigest(), chr(i))
#     return rtDecoded

# def seqDecode(rt):
#     rtDecoded = base64.b64decode(rt).decode('UTF-8')[:-4]
#     return rtDecoded