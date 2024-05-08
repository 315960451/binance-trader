# -*- coding: UTF-8 -*-
# @yasinkuyu

class Messages():
    ## use @staticmethod , so the funtion can be called without instantiating the class.
    @staticmethod
    def get(msg):
        print('Message : ' + msg)
        exit(1)
