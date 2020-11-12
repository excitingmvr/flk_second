# -- coding: utf-8 --

from flask import request
from user_agents import parse
import hashlib

from src.common.constants import Constants

constantsObj = Constants()

class Util():

    def getDeviceCd(self):
        userAgent = parse(request.user_agent.string)

        # print(userAgent.is_pc)
        # print(userAgent.is_mobile)
        # print(userAgent.is_tablet)

        if userAgent.is_pc:
            result = 1
        else:
            pass
        if userAgent.is_mobile:
            result = 2
        else:
            pass
        if userAgent.is_tablet:
            result = 3

        return result
    
    def setZerofill(self, param):
        if len(param) == 1:
            result = "0" + param
        else:
            result = param
        return result

    def setPathProject(self, param):
        if param == 'Windows':
            result = constantsObj.PATH_PROJECT_WINDOWS
        elif param == 'Linux':
            result = constantsObj.PATH_PROJECT_LINUX
        else:   # mac (Darwin)
            result = constantsObj.PATH_PROJECT_MAC
        return result
    
    def setPathSource(self, param):
        if param == 'Windows':
            result = constantsObj.PAHT_SOURCE_WINDOWS
        elif param == 'Linux':
            result = constantsObj.PAHT_SOURCE_LINUX
        else:   # mac (Darwin)
            result = constantsObj.PAHT_SOURCE_MAC
        return result

    def setPathUpload(self, param):
        if param == 'Windows':
            result = constantsObj.PATH_UPLOAD_WINDOWS
        elif param == 'Linux':
            result = constantsObj.PATH_UPLOAD_LINUX
        else:   # mac (Darwin)
            result = constantsObj.PATH_UPLOAD_MAC
        return result


    # def seqEncode(self, rt):
    #     return hashlib.md5(str(rt).encode()).hexdigest()


    # def seqDecode(self, rt):
    #     for i in range(123):
    #         rtDecoded = str(rt).replace(hashlib.md5(chr(i).encode()).hexdigest(), chr(i))
    #     return rtDecoded