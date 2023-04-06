import mysql.connector

from util.JsonConfparser import JsonConfigParser


class MysqlConnector:

    def __init__(self,dbname:str):
        parser = JsonConfigParser('database/database.json')
        conf = parser.readJsonConfig()

        if not conf:
            return None
        datasource = parser.jsondata['datasource']

        self.address = datasource['address']
        self.user = datasource['user']
        self.passwd = datasource['password']
        self.port = datasource['port']
        self.dbname = dbname
        self.connected = None
    def connect_db(self):
        self.connected = mysql.connector.connect(host=self.address,port=self.port,database=self.dbname,user=self.user,password=self.passwd)
    def find_db(self,str,values = None):
        try:
            self.connect_db()
            cursor = self.connected.cursor()
            if values == None:
                cursor.execute(str)
            else :
                cursor.execute(str, values)
            result = cursor.fetchall()
            self.connected.close()
            return result
        except Exception as e:
            print('SQL ERROR : ', e)

    def insert_db(self,str,values):
        try:
            self.connect_db()
            cursor = self.connected.cursor()
            cursor.execute(str, values)
            self.connected.commit()
            # print('Insert Database Completed')
            self.connected.close()
            return True
        except Exception as e:
            print('SQL ERROR : ',e)
            return False

    def destroy(self):
        del self
