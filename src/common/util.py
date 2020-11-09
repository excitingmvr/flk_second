# -- coding: utf-8 --

from flask import request
from user_agents import parse
import hashlib

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



    # def seqEncode(self, rt):
    #     return hashlib.md5(str(rt).encode()).hexdigest()


    # def seqDecode(self, rt):
    #     for i in range(123):
    #         rtDecoded = str(rt).replace(hashlib.md5(chr(i).encode()).hexdigest(), chr(i))
    #     return rtDecoded