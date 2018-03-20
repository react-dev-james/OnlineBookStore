'''
Created on 15-Mar-2016

@author: parkar_s
'''

class Category(object):
    '''
    classdocs
    '''


    def __init__(self, category_id,name ,sub_cat=None):
        '''
        Constructor
        '''
        self.id = category_id
        self.name=name
        if sub_cat:
            self.sub_category = sub_cat
        