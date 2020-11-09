# -- coding: utf-8 --

from flask import request
from random import *
import datetime, os

from src.common.constants import Constants
from src.common.util import Util
from src.common.database import Database
from src.common.commonSql import CommonSql

dt = datetime.datetime.now()

constantsObj = Constants()
utilObj = Util()
databaseObj = Database()
commonSqlObj = CommonSql()

class Common():

    def __init__(self, module):
        self.moduleListUrl = "/" + module + "/list"
        self.moduleFormUrl = "/" + module + "/form"
        self.moduleViewUrl = "/" + module + "/view"

        self.moduleListHtml = "/" + module + "/" + module + "List.html"
        self.moduleFormHtml = "/" + module + "/" + module + "Form.html"
        self.moduleViewHtml = "/" + module + "/" + module + "View.html"

    def uploadFile(self, inputName, module, lastrowid, tablePrefix):
        inputName = inputName
        fileKindCd = inputName[-1:]
        files = request.files.getlist(inputName)
        i = 0
        fileDefaultNy = 1
        filePathFull = constantsObj.UPLOAD_FOLDER_FULL + "/" + module + "/" + inputName + "/" + str(dt.year) + "/" + str(dt.month) + "/" + str(dt.day) + "/" + str(dt.hour)
        filePathForLink = constantsObj.UPLOAD_FOLDER_FOR_LINK + "/" + module + "/" + inputName + "/" + str(dt.year) + "/" + str(dt.month) + "/" + str(dt.day) + "/" + str(dt.hour)
        
        if os.path.isdir(filePathFull):
            pass
        else:
            os.makedirs(filePathFull)

        for file in files:
            if file.filename:
                file.save(os.path.join(filePathFull, file.filename))
                fileExtension = os.path.splitext(file.filename)[1]
                fileNameSystem = str(randint(1000, 9999)) + str(dt.year)[0:2] + utilObj.setZerofill(str(dt.month)) + utilObj.setZerofill(str(dt.day)) + utilObj.setZerofill(str(dt.hour)) + str(dt.microsecond)
                os.rename(filePathFull + "/" + file.filename, filePathFull + "/" + fileNameSystem + fileExtension)
                
                if i > 0:
                    defaultNy = 0
                else:
                    pass

                dicInsertFile = {
                                    "deftFileKindCd":fileKindCd,
                                    "deftFileDefaultNy":fileDefaultNy,
                                    "deftFilePath":filePathForLink,
                                    "deftFileNameOriginal":file.filename,
                                    "deftFileNameSystem":fileNameSystem,
                                    "deftFileExtension":fileExtension[1:],
                                    "deftFileSize":os.path.getsize(filePathFull + "/" + fileNameSystem + fileExtension),
                                    "deftFileOrder":i,
                                    "deftRegIp":request.environ["REMOTE_ADDR"],
                                    "deftRegSeq":0,
                                    "deftRegOffset":0,
                                    "deftRegDatetime":datetime.datetime.today(),
                                    "deftRegDeviceCd":utilObj.getDeviceCd(),                         
                                    "deftModIp":request.environ["REMOTE_ADDR"],
                                    "deftModSeq":0,
                                    "deftModOffset":0,
                                    "deftModDatetime":datetime.datetime.today(),
                                    "deftModDeviceCd":utilObj.getDeviceCd(),
                                    "deftSys":constantsObj.SYS_NUMBER,
                                    "deftDelNy":0,
                                    "deftUpperSeq":lastrowid
                                }   
                i = i + 1
                commonSqlObj.uploadFile(tablePrefix, (dicInsertFile))
            else:
                pass

    def getTotalFileSize(self, files):
        total = 0
        for file in files:
            total = total + file["deftFileSize"]
        return total

