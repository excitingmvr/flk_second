# -- coding: utf-8 --

import pymysql
 
class Database():
    def __init__(self):
        #<--
        self.dbConn= pymysql.connect(
                                host="34.64.150.241",
                                port=33067,
                                user="desk",
                                password="Cortkd11!!",
                                db="lamp",
                                charset='utf8'
                                )
        self.cursor= self.dbConn.cursor(pymysql.cursors.DictCursor)
 
    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeFetchOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeFetchAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit(self):
        self.dbConn.commit()

    def close(self):
        self.dbConn.close()

    def lastrowid(self):
        return self.cursor.lastrowid
        