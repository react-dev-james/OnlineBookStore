'''
Created on 15-Mar-2016

@author: parkar_s
'''
from contextlib import closing
from flask import jsonify
from bookstore.src.Database.DBConnection import DBConnect


class DataAccessor(object):
    '''
    classdocs
    '''

    _instance = None

    def __init__(self):
        '''
        Constructor
        '''
        self.connection = DBConnect().get_connection()

    def read(self, table=None, columns=None, where_row=None, query=None):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(query)
            data_list = cursor.fetchall()
            return data_list
