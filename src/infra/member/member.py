# -- coding: utf-8 --

from flask import Blueprint, render_template, redirect, request
from werkzeug.utils import secure_filename
from random import *
import datetime, math, base64, bcrypt, os

from src.common.filter import *
from src.common.constants import Constants
from src.common.common import Common
from src.common.util import Util
from src.common.database import Database
from src.common.commonSql import CommonSql
#<--
from src.infra.member.memberSql import MemberSql as ModuleSql

dt = datetime.datetime.now()

#<--
module = "member"   

constantsObj = Constants()
commonObj = Common(module)
databaseObj = Database()
moduleSqlObj = ModuleSql()
commonSqlObj = CommonSql()
utilObj = Util()

#<--
member = Blueprint(module, __name__, url_prefix = "/" + module)
#<--
moduleObj = member

####################################################################### 

@moduleObj.route("/list", methods=["GET"])
def moduleList():

    if request.args.get("searchOption"):
        dicSchsMain = {"searchOption":request.args.get("searchOption"), "searchValue":request.args.get("searchValue")}
    else:
        dicSchsMain = {"searchOption":None, "searchValue":None}

    print(dicSchsMain)

    pageThis = request.args.get("pageThis") if request.args.get("pageThis") else 1
    pageThis = int(pageThis)
    limitStart = ((pageThis - 1) * constantsObj.rowNum)
    # print(dicSchsMain)
    rowTotal = moduleSqlObj.getRowTotal(dicSchsMain)
    rows = moduleSqlObj.getRows(limitStart, dicSchsMain)
    
    pageTotal = math.ceil(rowTotal["rowTotal"] / constantsObj.rowNum)
    
    blockTotal = math.ceil(pageTotal / constantsObj.pageNum)
    blockThis = math.ceil(pageThis / constantsObj.pageNum)

    pageFirst = (((math.ceil(pageThis / constantsObj.pageNum)-1)*constantsObj.pageNum)+1)
    pageEnd = pageFirst + constantsObj.pageNum -1
    
    if pageTotal < pageEnd:
        pageEnd = pageTotal
    else:
        pass
    
    pagePrevious = pageFirst - 1
    pageNext = pageEnd + 1

    dicPagsMain = {
                    "rowTotal":rowTotal["rowTotal"],
                    "pageTotal":pageTotal,
                    "pageThis":pageThis,
                    "blockTotal":blockTotal,
                    "blockThis":blockThis,
                    "pageFirst":pageFirst,
                    "pageEnd":pageEnd,
                    "pagePrevious":pagePrevious,
                    "pageNext":pageNext,
                    "pageNum":constantsObj.pageNum,            
    }

    return render_template(commonObj.moduleListHtml,
                            rts=rows,
                            dicPagsMain=dicPagsMain,
                            dicSchsMain = dicSchsMain
                            )


@moduleObj.route("/view")
def moduleView():
    row = moduleSqlObj.getRow(seqDecode(request.args.get('seq')))

    #<-- if attached files are exist
    files1 = commonSqlObj.getFiles("infrmember", seqDecode(request.args.get('seq')), 1)
    files1TotalSize = commonObj.getTotalFileSize(files1)
    files2 = commonSqlObj.getFiles("infrmember", seqDecode(request.args.get('seq')), 2)
    files2TotalSize = commonObj.getTotalFileSize(files2)
    #<-- if attached files are exist end
    #<--
    return render_template(commonObj.moduleViewHtml, rt = row, rtFiles1 = files1, rtFiles1TotalSize = files1TotalSize, rtFiles2 = files2, rtFiles2TotalSize = files2TotalSize,)
    # return render_template(commonObj.moduleViewHtml, rt = row)


@moduleObj.route("/form")   
def moduleForm():
    totalabc = 0
    if request.args.get("seq") is None:
        row = None
        return render_template(commonObj.moduleFormHtml, rt = row)
    else:
        row = moduleSqlObj.getRow(seqDecode(request.args.get("seq")))
        #<-- if attached files are exist
        files1 = commonSqlObj.getFiles("infrmember", seqDecode(request.args.get('seq')), 1)
        files1TotalSize = commonObj.getTotalFileSize(files1)
        files2 = commonSqlObj.getFiles("infrmember", seqDecode(request.args.get('seq')), 2)
        files2TotalSize = commonObj.getTotalFileSize(files2)
        #<-- if attached files are exist end
        return render_template(commonObj.moduleFormHtml, rt = row, rtFiles1 = files1, rtFiles1TotalSize = files1TotalSize, rtFiles2 = files2, rtFiles2TotalSize = files2TotalSize)
    

## db process #################################################

@moduleObj.route("/insert", methods=['POST'])
def moduleInsert():
    strSchMain = setStrSchForPostMain(request.form['searchOption'], request.form['searchValue'])
    #<-
    dicInsertMain = {
                        "ifmbAdminNy":request.form["ifmbAdminNy"],
                        "ifmbFirstName":request.form["ifmbFirstName"],
                        "ifmbLastName":request.form["ifmbLastName"],
                        "ifmbId":request.form["ifmbId"],
                        "ifmbPassword":bcrypt.hashpw(request.form["ifmbPassword"].encode('utf-8'), bcrypt.gensalt()),
                        "ifmbGenderCd":request.form["ifmbGenderCd"],
                        "ifmbDob":datetime.datetime(int(request.form["dobYear"]), 
                                                    int(request.form["dobMonth"]), 
                                                    int(request.form["dobDay"])),
                        "ifmbEmailAuthNy":request.form["ifmbEmailAuthNy"],
                        "ifmbNickName":request.form["ifmbNickName"],
                        "ifmbDormantNy":0,
                        "ifmbIntroduction":request.form["ifmbIntroduction"],
                        "ifmbRegIp":request.environ["REMOTE_ADDR"],
                        "ifmbRegSeq":0,
                        "ifmbRegOffset":0,
                        "ifmbRegDatetime":datetime.datetime.today(),
                        "ifmbRegDeviceCd":utilObj.getDeviceCd(),                         
                        "ifmbModIp":request.environ["REMOTE_ADDR"],
                        "ifmbModSeq":0,
                        "ifmbModOffset":0,
                        "ifmbModDatetime":datetime.datetime.today(),
                        "ifmbModDeviceCd":utilObj.getDeviceCd(),
                        "ifmbSys":constantsObj.SYS_NUMBER,
                        "ifmbDelNy":0                
                    }
    lastrowid = moduleSqlObj.insert((dicInsertMain))
    # #<- if attached files existed
    commonObj.uploadFile("file1", module, lastrowid, "infrmember")
    commonObj.uploadFile("file2", module, lastrowid, "infrmember")
    #<- if attached files existed end
    return redirect(commonObj.moduleViewUrl + "?pageThis=" + request.form["pageThis"] + "&seq=" + seqEncode(lastrowid) + strSchMain)


@moduleObj.route("/update", methods=['POST'])
def moduleUpdate():
    strSchMain = setStrSchForPostMain(request.form['searchOption'], request.form['searchValue'])
    #<-
    dicUpdateMain = {
                        "ifmbAdminNy":request.form["ifmbAdminNy"],
                        "ifmbFirstName":request.form["ifmbFirstName"],
                        "ifmbLastName":request.form["ifmbLastName"],
                        "ifmbId":request.form["ifmbId"],
                        "ifmbPassword":request.form["ifmbPassword"],
                        "ifmbGenderCd":request.form["ifmbGenderCd"],
                        "ifmbDob":datetime.datetime(int(request.form["dobYear"]), 
                                                    int(request.form["dobMonth"]), 
                                                    int(request.form["dobDay"])),
                        "ifmbEmailAuthNy":request.form["ifmbEmailAuthNy"],
                        "ifmbNickName":request.form["ifmbNickName"],
                        "ifmbDormantNy":0,
                        "ifmbIntroduction":request.form["ifmbIntroduction"],
                        "ifmbModIp":request.environ["REMOTE_ADDR"],
                        "ifmbModSeq":1,
                        "ifmbModOffset":1,
                        "ifmbModDatetime":datetime.datetime.today(),
                        "ifmbModDeviceCd":utilObj.getDeviceCd(),
                        "ifmbSeq":seqDecode(request.form["ifmbSeq"])
    }
    moduleSqlObj.update((dicUpdateMain))
    return redirect(commonObj.moduleViewUrl + "?pageThis=" + request.form["pageThis"] + "&seq=" + request.form["seq"] + strSchMain)


@moduleObj.route("/uelete", methods=['GET'])
def moduleUelete():
    strSchMain = setStrSchForGetMain()
    moduleSqlObj.uelete(seqDecode(request.args.get('seq')))
    return redirect(commonObj.moduleListUrl + "?pageThis=" + request.args.get("pageThis") + strSchMain)


@moduleObj.route("/delete", methods=['GET'])
def moduleDelete():
    strSchMain = setStrSchForGetMain()
    moduleSqlObj.delete(seqDecode(request.args.get('seq')))
    return redirect(commonObj.moduleListUrl + "?pageThis=" + request.args.get("pageThis") + strSchMain) 


@moduleObj.route("/ajxCheckId", methods=['POST'])
def ajxCheckId():
    return str(moduleSqlObj.getRowCount(request.form['Id'])['rowCount'])
    

## utils ########################################

def setStrSchForGetMain():
    
    if request.args.get("searchOption") == 'None' or request.args.get("searchOption") == None:
        strSchsMain = ''
    else:
        strSchsMain = "&searchOption=" + request.args.get("searchOption") + "&searchValue=" + request.args.get("searchValue")
    return strSchsMain

def setStrSchForPostMain(searchOption, searchValue):
    if searchOption == 'None' or searchOption == None:
        strSchsMain = ''
    else:
        strSchsMain = '&searchOption=' + searchOption + '&searchValue=' + searchValue
    return strSchsMain

# data = request.form
# for key in data:
#     print ("form key " + key + " " + data[key])

# @moduleObj.after_app_request
# def after_app_request(response):
#     print("after_app_request")
#     return response

# @moduleObj.after_request
# def after_request(response):
#     print("after_request")
#     return response

# @moduleObj.after_request
# def after_request(response):
#     # databaseObj.commit()
#     if databaseObj.dbConn:
#         print("yes")
#         print(databaseObj.dbConn)
#         # databaseObj.close()
#     else:
#         print("no")
#         # pass
#     return response


# @moduleObj.after_app_request
# def after_app_request(response):
#     # databaseObj.commit()
#     if databaseObj.dbConn:
#         print("yes")
#         print(databaseObj.dbConn)
#         # databaseObj.close()
#     else:
#         print("no")
#         # pass
#     return response

# @moduleObj.after_request
# def set_response_headers(r):
#     r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
#     r.headers['Pragma'] = 'no-cache'
#     r.headers['Expires'] = '0'
#     return r

# @moduleObj.after_request
# def add_header(response):
#     print("after_request")
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Pragma"] = "no-cache"
#     response.headers["Expires"] = "0"
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response

    # databaseObj.execute(moduleSqlObj.update,(
    #                                         request.form["ifmbAdminNy"],
    #                                         request.form["ifmbFirstName"],
    #                                         request.form["ifmbLastName"],
    #                                         request.form["ifmbId"],
    #                                         request.form["ifmbPassword"],
    #                                         request.form["ifmbGenderCd"],
    #                                         datetime.datetime(int(request.form["dobYear"]), 
    #                                                             int(request.form["dobMonth"]), 
    #                                                             int(request.form["dobDay"])),
    #                                         request.form["ifmbEmailAuthNy"],
    #                                         request.form["ifmbNickName"],
    #                                         0,
    #                                         request.environ["REMOTE_ADDR"],
    #                                         1,
    #                                         1,
    #                                         datetime.datetime.today(),
    #                                         utilObj.getDeviceCd(),
    #                                         request.form["ifmbSeq"]
    #                                         ))

        # return render_template(commonObj.moduleListHtml,
    #                         results=rows,
    #                         rowTotal = rowTotal["rowTotal"], 
    #                         pageTotal = pageTotal,
    #                         pageThis=pageThis,
    #                         blockTotal = blockTotal,
    #                         blockThis = blockThis,
    #                         pageFirst = pageFirst,
    #                         pageEnd = pageEnd,
    #                         pagePrevious = pagePrevious,
    #                         pageNext = pageNext,
    #                         pageNum = constantsObj.pageNum
    #                         )

    # databaseObj.execute(moduleSqlObj.insert,(
    #                                     request.form["ifmbAdminNy"],
    #                                     request.form["ifmbFirstName"],
    #                                     request.form["ifmbLastName"],
    #                                     request.form["ifmbId"],
    #                                     request.form["ifmbPassword"],
    #                                     request.form["ifmbGenderCd"],
    #                                     datetime.datetime(int(request.form["dobYear"]), 
    #                                                         int(request.form["dobMonth"]), 
    #                                                         int(request.form["dobDay"])),
    #                                     request.form["ifmbEmailAuthNy"],
    #                                     request.form["ifmbNickName"],
    #                                     0,
    #                                     request.environ["REMOTE_ADDR"],
    #                                     1,
    #                                     1,
    #                                     datetime.datetime.today(),
    #                                     utilObj.getDeviceCd(),
    #                                     request.environ["REMOTE_ADDR"],
    #                                     1,
    #                                     1,
    #                                     datetime.datetime.today(),
    #                                     utilObj.getDeviceCd(),
    #                                     constantsObj.SYS_NUMBER,
    #                                     0
    #                                 )) 


    # password = 'pass1234'  #2
    # b = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())   #3 
    # print(b)

    # c = 'password1234'
    # print(bcrypt.checkpw(c.encode('utf-8'), b))

    # d = 'password123'
    # print(bcrypt.checkpw(d.encode('utf-8'), b))

    # e = 'pass1234'
    # print(bcrypt.checkpw(e.encode('utf-8'), b))