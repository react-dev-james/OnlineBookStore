'''
Created on 20-Jul-2016

@author: Dell
'''

import datetime
import random
import pymysql
from bookstore.config import userid
from bookstore.src.dao.DataAccessor import DataAccessor


class WishlistDao(DataAccessor):
    '''
    classdocs
    '''

    def __init__(self):
        super(WishlistDao, self).__init__()

    def getWishlist(self):
        try:
            query = ("select w.*,b.ISBN, title, authors, publisher, "
                     "DATE_FORMAT(yop,'%Y-%m-%d') as yop, "
                     "available_copies, price, format, keywords, subject,image_loc "
                     "from wishlist as w left join books as b "
                     "on b.ISBN=w.isbn where user_id='{}'").format(userid)
            result = super(WishlistDao, self).read(query=query)
            for i in result:
                q = (
                    "select * from rating where isbn='{}'").format(i.get('isbn'))
                rt = super(WishlistDao, self).read(query=q)
                i['rating'] = rt

            return result
        except Exception as e:
            print(e, 'in getwishlist')
            return []

    def addToWishlist(self, isbn, userid):
        getQuery = (
            "select * from wishlist where user_id='{}'").format(userid)
        getResult = super(WishlistDao, self).read(query=getQuery)
        wishlist_id = str(random.randint(0, 9999999))
        userQuery = (
            "select * from customer where Login_id='{}'").format(userid)
        userData = super(WishlistDao, self).read(query=userQuery)

        wishListName = userData[0].get('Name').split(' ')[0] + "s wishlist"

        if len(getResult) > 0:
            wishlist_id = getResult[0].get('wishlist_id')
        query = ("insert into wishlist(user_id, wishlist_id,isbn,name) values('{}','{}','{}','{}')").format(
            userid, wishlist_id, isbn, wishListName)
        super(WishlistDao, self).read(query=query)

    def removefromWishList(self, i, userid):
        query = ("delete from wishlist where id ={} and user_id='{}'").format(
            i, userid)
        super(WishlistDao, self).read(query=query)

    def updateWishlist(self, i=None, isbn=None, operationType='add'):
        try:
            if operationType == 'add':
                self.addToWishlist(isbn, userid)

            else:
                self.removefromWishList(i, userid)
        except Exception as e:
            print(e)
            return []
