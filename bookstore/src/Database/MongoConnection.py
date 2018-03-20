from pymongo import MongoClient
from bookstore.src.config import DatabaseConfig
# Connect to the database

class DBConnect(object):
    _instance = None
    connection = None
   
    def __init__(self):
        '''Returns a database connection/handle given the dsn
    
        This function saves the database connection, so if you
        invoke this again, it gives you the same one, rather
        than making a second connection.  This is the so-called
        Singleton pattern.'''
        if not self.connection:
            try:
                
                
                self.client = MongoClient("mongodb://localhost:27017/")
                self.database = self.client[DatabaseConfig.DB_NAME]
                # so modifications take effect automatically
            except Exception as e:
                print ("Couldn't connect to database. MongoDB error %d: %s" %
                       (e.args[0], e.args[1]))
        
   
    
    def get_db(self):
        '''
            @return databse instance established 
        ''' 
        return self.client[DatabaseConfig.DB_NAME]
    
    def get_col(self, name):
        '''return the collection instance''' 
        return self.database[name]