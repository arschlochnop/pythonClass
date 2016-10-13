#!/usr/bin/env python
# encoding: utf-8

"""
@time: 16-10-8 下午7:06
@author: Arschloch(xx@nop.pw)
@version: 1.0.0
"""

import MySQLdb

class MySQL(object):
    """
        Python Class for connecting  with MySQL server and accelerate development project using MySQL
        Extremely easy to learn and use, friendly construction.
    """
    __instance   = None
    __dbconfig   = None
    __session    = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
             cls.__instance = super(MySQL, cls).__new__(cls,*args,**kwargs)
        return cls.__instance
    ## End def __new__

    def __init__(self, dbconfig):
        self.__dbconfig = dbconfig
    ## End def __init__

    def __open(self):
        try:
            cnx = MySQLdb.connect(host = self.__dbconfig['host'],
                     port = self.__dbconfig['port'],
                     user = self.__dbconfig['user'],
                     passwd = self.__dbconfig['passwd'],
                     db = self.__dbconfig['db'],
                     charset = self.__dbconfig['charset'])
            self.__connection = cnx
            self.__session    = cnx.cursor()
        except MySQLdb.Error as e:
            print "Error %d: %s" % (e.args[0],e.args[1])
    ## End def __open

    def __close(self):
        self.__session.close()
        self.__connection.close()
    ## End def __close

    def select(self, query,convert=False):
        self.__open()
        self.__session.execute(query)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)
        result = ""
        if number_rows > 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        elif number_rows > 1 and number_columns == 1:
            result = [item[0] for item in self.__session.fetchall()]
        elif number_rows == 1:
            if convert:
                result = self.__session.fetchone()
            else:
                result = list(self.__session.fetchone())
        self.__close()
        return result
    ## End def select

    def update(self, query):
        self.__open()
        self.__session.execute(query)
        self.__connection.commit()

        # Obtain rows affected
        update_rows = self.__session.rowcount
        self.__close()

        return update_rows
    ## End function update

    def insert(self, query):
        self.__open()
        self.__session.execute(query)
        self.__connection.commit()
        self.__close()
        return self.__session.lastrowid
    ## End def insert

    def delete(self, query):
        self.__open()
        self.__session.execute(query)
        self.__connection.commit()

        # Obtain rows affected
        delete_rows = self.__session.rowcount
        self.__close()

        return delete_rows
    ## End def delete

    def filter(text):
        return MySQLdb.escape_string(text)
## End class