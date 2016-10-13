#!/usr/bin/env python
# encoding: utf-8

"""
@time: 16-10-12 下午5:21
@author: Arschloch(xx@nop.pw)
@version: 1.0.0
"""

import redis

class REDIS():

    __host = None
    __port = None
    __db = None
    __connection = None


    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
            cls.__instance = super(REDIS, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

## End def __new__

    def __init__(self,host,port=6379,db=0):
        self.__host = host
        self.__port = port
        self.__db = db


    def cmd(self,command, *args):
        connection = redis.Connection(host=self.__host, port=self.__port, db=self.__db)
        try:
            connection.connect()
            connection.send_command(command, *args)

            response = connection.read_response()
            if command in redis.Redis.RESPONSE_CALLBACKS:
                return redis.Redis.RESPONSE_CALLBACKS[command](response)
            return response

        finally:
            del connection





