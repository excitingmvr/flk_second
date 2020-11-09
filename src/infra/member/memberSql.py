# -- coding: utf-8 --

from src.common.constants import Constants
from src.common.database import Database

constantsObj = Constants()
databaseObj = Database()

class MemberSql():
    #<--
    prefix = "ifmb"
    #<--
    common_insert = prefix + "RegIp," \
                    + prefix + "RegSeq," \
                    + prefix + "RegOffset," \
                    + prefix + "RegDatetime," \
                    + prefix + "RegDeviceCd," \
                    + prefix + "ModIp," \
                    + prefix + "ModSeq," \
                    + prefix + "ModOffset," \
                    + prefix + "ModDatetime," \
                    + prefix + "ModDeviceCd," \
                    + prefix + "Sys," \
                    + prefix + "DelNy"


    def getRow(self, seq):
        #<--
        sqlSelectOne = """
                        SELECT *
                        FROM 
                            infrmember 
                        where 1=1 
                            and ifmbSeq = %s 
                        """
        return databaseObj.executeFetchOne(sqlSelectOne,(seq))


    def getRowCount(self, Id):
        #<--
        sqlSelectOne = """
                        SELECT count(ifmbSeq) as rowCount
                        FROM 
                            infrmember 
                        where 1=1 
                            and ifmbDelNy = 0
                            and ifmbId = %s 
                        """
        return databaseObj.executeFetchOne(sqlSelectOne,(Id))        


    def insert(self, dicInsertMain):
        #<--
        sqlInsert = """
                        INSERT INTO infrmember
                        (
                            ifmbAdminNy,
                            ifmbFirstName,
                            ifmbLastName,
                            ifmbId,
                            ifmbPassword,
                            ifmbGenderCd,
                            ifmbDob,
                            ifmbEmailAuthNy,
                            ifmbNickName,
                            ifmbDormantNy,
                            ifmbIntroduction,
                    """ + self.common_insert + \
                    """
                        )
                        VALUES
                        ( 
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        #<--
        databaseObj.execute(sqlInsert, (
                                        dicInsertMain["ifmbAdminNy"],
                                        dicInsertMain["ifmbFirstName"],
                                        dicInsertMain["ifmbLastName"],
                                        dicInsertMain["ifmbId"],
                                        dicInsertMain["ifmbPassword"],
                                        dicInsertMain["ifmbGenderCd"],
                                        dicInsertMain["ifmbDob"],
                                        dicInsertMain["ifmbEmailAuthNy"],
                                        dicInsertMain["ifmbNickName"],
                                        dicInsertMain["ifmbDormantNy"],
                                        dicInsertMain["ifmbIntroduction"],
                                        dicInsertMain["ifmbRegIp"],
                                        dicInsertMain["ifmbRegSeq"],
                                        dicInsertMain["ifmbRegOffset"],
                                        dicInsertMain["ifmbRegDatetime"],
                                        dicInsertMain["ifmbRegDeviceCd"],
                                        dicInsertMain["ifmbModIp"],
                                        dicInsertMain["ifmbModSeq"],
                                        dicInsertMain["ifmbModOffset"],
                                        dicInsertMain["ifmbModDatetime"],
                                        dicInsertMain["ifmbModDeviceCd"],
                                        dicInsertMain["ifmbSys"],
                                        dicInsertMain["ifmbDelNy"],
                                        ))
        lastrowid = databaseObj.lastrowid()
        databaseObj.commit()
        return lastrowid


    def getWherePhrase(self, dicSchsMain):
        if dicSchsMain["searchOption"] == None:
            wherePhrase = ""
        else:
            wherePhrase = "and " + dicSchsMain["searchOption"] + " like '%%" + dicSchsMain["searchValue"] + "%%'"
        return wherePhrase


    def getRowTotal(self, dicSchsMain):
        wherePhraseRt = self.getWherePhrase(dicSchsMain)
        #<--
        return databaseObj.executeFetchOne("select count(ifmbSeq)as rowTotal from infrmember where 1=1 " + wherePhraseRt)


    def getRows(self, limitStart, dicSchsMain):
        wherePhraseRt = self.getWherePhrase(dicSchsMain)
        #<--
        sqlSelectRows = """                                                       
                            select *
                            from 
                                infrmember
                            where 1=1
                        """ + wherePhraseRt + \
                        """
                            order by ifmbRegDatetime desc
                            limit %s, %s
                        """
        return databaseObj.executeFetchAll(sqlSelectRows,(limitStart, constantsObj.rowNum))
    
    def uelete(self, seq):
        #<--
        sqlUelete = """
                        update
                            infrmember
                        set
                            ifmbDelNy = 1
                        where
                            ifmbSeq = %s
                    """
        databaseObj.execute(sqlUelete, (seq))
        databaseObj.commit()
        

    def delete(self, seq):
        #<--
        sqlDelete = """
                        delete from infrmember where ifmbSeq = %s
                    """
        databaseObj.execute(sqlDelete, (seq))
        databaseObj.commit()
    
    
    def update(self, dicUpdateMain):
        #<--
        sqlUpdate = """
                        update infrmember
                        set
                            ifmbAdminNy = %s,
                            ifmbFirstName = %s,
                            ifmbLastName = %s,
                            ifmbId = %s,
                            ifmbPassword = %s,
                            ifmbGenderCd = %s,
                            ifmbDob = %s,
                            ifmbEmailAuthNy = %s,
                            ifmbNickName = %s,
                            ifmbDormantNy = %s,
                            ifmbIntroduction = %s,
                            ifmbModIp = %s,
                            ifmbModSeq = %s,
                            ifmbModOffset = %s,
                            ifmbModDatetime = %s,
                            ifmbModDeviceCd = %s
                        where ifmbSeq = %s
                    """
        #<--
        databaseObj.execute(sqlUpdate, (
                                        dicUpdateMain["ifmbAdminNy"],
                                        dicUpdateMain["ifmbFirstName"],
                                        dicUpdateMain["ifmbLastName"],
                                        dicUpdateMain["ifmbId"],
                                        dicUpdateMain["ifmbPassword"],
                                        dicUpdateMain["ifmbGenderCd"],
                                        dicUpdateMain["ifmbDob"],
                                        dicUpdateMain["ifmbEmailAuthNy"],
                                        dicUpdateMain["ifmbNickName"],
                                        dicUpdateMain["ifmbDormantNy"],
                                        dicUpdateMain["ifmbIntroduction"],
                                        dicUpdateMain["ifmbModIp"],
                                        dicUpdateMain["ifmbModSeq"],
                                        dicUpdateMain["ifmbModOffset"],
                                        dicUpdateMain["ifmbModDatetime"],
                                        dicUpdateMain["ifmbModDeviceCd"],
                                        dicUpdateMain["ifmbSeq"],
                                        ))
        databaseObj.commit()



        # for key, val in dicInsertFile.items():
        #     print("key = {key}, value={value}".format(key=key,value=val))

        # print(sqlInsertFile)
    # getOne1 = """
    #             SELECT *
    #             FROM 
    #                 infrmember 
    #             where 1=1 
    #                 and ifmbSeq = %s 
    #        """

    # update1 = """
    #             update infrmember
    #             set
    #                 ifmbAdminNy = %s,
    #                 ifmbFirstName = %s,
    #                 ifmbLastName = %s,
    #                 ifmbId = %s,
    #                 ifmbPassword = %s,
    #                 ifmbGenderCd = %s,
    #                 ifmbDob = %s,
    #                 ifmbEmailAuthNy = %s,
    #                 ifmbNickName = %s,
    #                 ifmbDormantNy = %s,
    #                 ifmbModIp = %s,
    #                 ifmbModSeq = %s,
    #                 ifmbModOffset = %s,
    #                 ifmbModDatetime = %s,
    #                 ifmbModDeviceCd = %s
    #             where ifmbSeq = %s
    #         """
    # insert1 = """
    #             INSERT INTO infrmember
    #             (
    #                 ifmbAdminNy,
    #                 ifmbFirstName,
    #                 ifmbLastName,
    #                 ifmbId,
    #                 ifmbPassword,
    #                 ifmbGenderCd,
    #                 ifmbDob,
    #                 ifmbEmailAuthNy,
    #                 ifmbNickName,
    #                 ifmbDormantNy,
    #         """ + common_insert + \
    #         """
    #             )
    #             VALUES
    #             ( 
    #                 %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    #         """ 
    # rowTotal = "select count(ifmbSeq)as rowTotal from infrmember"    