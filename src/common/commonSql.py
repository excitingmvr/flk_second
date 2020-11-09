# -- coding: utf-8 --

from src.common.database import Database

databaseObj = Database()

class CommonSql():

    def uploadFile(self, tablePrefix, dicInsertFile):
        tableName = tablePrefix + "_attached"
        sqlInsertFile = """
                            insert into 
                        """ + tableName + \
                        """
                            (
                                deftFileKindCd,
                                deftFileDefaultNy,
                                deftFilePath,
                                deftFileNameOriginal,
                                deftFileNameSystem,
                                deftFileExtension,
                                deftFileSize,
                                deftFileOrder,
                                deftRegIp,
                                deftRegSeq,
                                deftRegOffset,
                                deftRegDatetime,
                                deftRegDeviceCd,
                                deftModIp,
                                deftModSeq,
                                deftModOffset,
                                deftModDatetime,
                                deftModDeviceCd,
                                deftSys,
                                deftDelNy,
                                deftUpperSeq
                            )
                            values(
                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
        databaseObj.execute(sqlInsertFile, (
                                            dicInsertFile["deftFileKindCd"],
                                            dicInsertFile["deftFileDefaultNy"],
                                            dicInsertFile["deftFilePath"],
                                            dicInsertFile["deftFileNameOriginal"],
                                            dicInsertFile["deftFileNameSystem"],
                                            dicInsertFile["deftFileExtension"],
                                            dicInsertFile["deftFileSize"],
                                            dicInsertFile["deftFileOrder"],
                                            dicInsertFile["deftRegIp"],
                                            dicInsertFile["deftRegSeq"],
                                            dicInsertFile["deftRegOffset"],
                                            dicInsertFile["deftRegDatetime"],
                                            dicInsertFile["deftRegDeviceCd"],
                                            dicInsertFile["deftModIp"],
                                            dicInsertFile["deftModSeq"],
                                            dicInsertFile["deftModOffset"],
                                            dicInsertFile["deftModDatetime"],
                                            dicInsertFile["deftModDeviceCd"],
                                            dicInsertFile["deftSys"],
                                            dicInsertFile["deftDelNy"],
                                            dicInsertFile["deftUpperSeq"],
                                            ))
        databaseObj.commit()


    def getFiles(self, tablePrefix, seq, kind):
        tableName = tablePrefix + "_attached"
        sqlSelectFiles = """
                            select
                                deftSeq
                                , deftFileKindCd
                                , deftFileDefaultNy
                                , deftFilePath
                                , deftFileNameOriginal
                                , deftFileNameSystem
                                , deftFileExtension
                                , deftFileSize
                                , deftFileOrder
                            from
                            """ + tableName + \
                            """
                            where 1=1
                                and deftUpperSeq = %s
                                and deftFileKindCd = %s
                                and deftDelNy = 0
                            order by
                                deftFileOrder
                        """
        return databaseObj.executeFetchAll(sqlSelectFiles,(seq, kind))

    def getTotalFilesSize(self, tablePrefix, seq, kind):
        tableName = tablePrefix + "_attached"
        sqlTotalFilesSize = """
                                select
                                    sum(deftFileSize) as totalFileSize
                            """ + tableName + \
                            """
                                where 1=1
                                    and deftUpperSeq = %s
                                    and deftFileKindCd = %s
                                    and deftDelNy = 0
                                order by
                                    deftFileOrder
                            """