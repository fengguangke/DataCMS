from pymongo import MongoClient
from flask import current_app

class UserModel():


    def __init__(self,*args,**kwargs):
        mongo_url = current_app.config['MONGO_URL']
        self._mongo =  MongoClient(mongo_url)


    @staticmethod
    def getUser(username):
        '''
        get userView from mongodb by username
        :param username:
        :return:
        '''
        user = {'name':'fengguangke',
                'password':'xx'}
        return user

    def insert(self,user):
        #TODO INSERT USER INGO DB
        pass

