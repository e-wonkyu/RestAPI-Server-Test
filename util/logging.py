import datetime
import getpass

from database.mysqlConnector import MysqlConnector
from util.JsonConfparser import JsonConfigParser
from util.mutex import Mutex
from util.timeutil import get_timestamp

"""
    Log Level
"""

WARNING = 0
ERROR = 1
INFO = 2
CRITICAL = 3
DEBUG = 4

level = ["WARNING","ERROR","INFO","CRITICAL","DEBUG"]

"""
    Mode
"""
MODE_DB = 0
MODE_File = 1

mode = ['db','file']


class Log:
    def __init__(self,mode=0,logdb='serverlog'):
        try:
            self.sql = MysqlConnector(logdb)
            if not self.sql:
                raise Exception("SQL Connector is Not Initialized")
            self.logformat = '[{0}]:{1}:{2}:{3}:{4}'
            self.mode = mode
            self.mutex = Mutex()
        except Exception as e:
            print("Log Error : ",e)
            return None

    def info(self,data:str,request=None):
        now = get_timestamp()
        self.mutex.lock()
        if self.mode == 0:
            query = 'insert into restapi_test values (%s,%s,%s,%s,%s,%s)'
            if request != None:
                logstr = self.logformat.format(level[INFO],
                                               getpass.getuser(),
                                               now,
                                               data,request.url)
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.datetime.now(),
                        data,
                        request.url
                    )
            else:
                logstr = self.logformat.format(level[INFO],
                                               getpass.getuser(),
                                               now,
                                               data,'')
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.now(),
                        data
                        ,0
                    )

            self.sql.insert_db(query, params)
        self.mutex.unlock()
        print(logstr)
    def error(self,data:str,request=None):
        now = get_timestamp()
        self.mutex.lock()
        if self.mode == 0:
            query = 'insert into restapi_test values (%s,%s,%s,%s,%s,%s)'
            if request != None:
                logstr = self.logformat.format(level[ERROR],
                                               getpass.getuser(),
                                               now,
                                               data,request.url)
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.datetime.now(),
                        data,
                        request.url
                    )
            else:
                logstr = self.logformat.format(level[INFO],
                                               getpass.getuser(),
                                               now,
                                               data,'')
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.now(),
                        data
                        ,0
                    )

            self.sql.insert_db(query, params)
        self.mutex.unlock()
        print(logstr)

    def debug(self,data:str,request=None):
        now = get_timestamp()
        self.mutex.lock()
        if self.mode == 0:
            query = 'insert into restapi_test values (%s,%s,%s,%s,%s,%s)'
            if request != None:
                logstr = self.logformat.format(level[ERROR],
                                               getpass.getuser(),
                                               now,
                                               data,request.url)
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.datetime.now(),
                        data,
                        request.url
                    )
            else:
                logstr = self.logformat.format(level[INFO],
                                               getpass.getuser(),
                                               now,
                                               data,'')
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.now(),
                        data
                        ,0
                    )

            self.sql.insert_db(query, params)
        self.mutex.unlock()
        print(logstr)
    def warning(self,data:str,request=None):
        now = get_timestamp()
        self.mutex.lock()
        if self.mode == 0:
            query = 'insert into restapi_test values (%s,%s,%s,%s,%s,%s)'
            if request != None:
                logstr = self.logformat.format(level[ERROR],
                                               getpass.getuser(),
                                               now,
                                               data,request.url)
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.datetime.now(),
                        data,
                        request.url
                    )
            else:
                logstr = self.logformat.format(level[INFO],
                                               getpass.getuser(),
                                               now,
                                               data,'')
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.now(),
                        data
                        ,0
                    )

            self.sql.insert_db(query, params)
        self.mutex.unlock()
        print(logstr)
    def critical(self,data:str,request=None):
        now = get_timestamp()
        self.mutex.lock()
        if self.mode == 0:
            query = 'insert into restapi_test values (%s,%s,%s,%s,%s,%s)'
            if request != None:
                logstr = self.logformat.format(level[ERROR],
                                               getpass.getuser(),
                                               now,
                                               data,request.url)
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.datetime.now(),
                        data,
                        request.url
                    )
            else:
                logstr = self.logformat.format(level[INFO],
                                               getpass.getuser(),
                                               now,
                                               data,'')
                params = \
                    (0,
                        level[INFO],
                        getpass.getuser(),
                        datetime.now(),
                        data
                        ,0
                    )

            self.sql.insert_db(query, params)
        self.mutex.unlock()
        print(logstr)