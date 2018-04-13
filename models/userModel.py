# coding=utf-8

from pymongo import MongoClient
from flask import current_app

class UserModel():
    '''
    user model
    user structure like:
    user = {'name':'xx',
            'password','',
            'age',23,
            'sex',男,
            'phone','12300000000',
            'address','',
            'email','1@123.com',
            'qq':'454362146'.
            'avatar':'avatar.png'
            }
    '''

    def __init__(self,*args,**kwargs):
        mongo_url = current_app.config['MONGO_URL']
        self._mongo =  MongoClient(mongo_url)

    @staticmethod
    def getUser(username):
        '''
        get user from mongodb by username
        :param username:
        :return:
        '''
        # todo get a user from db
        user = {'name':'fengguangke',
                'password':'xx'}
        return user

    def insert(self,user):
        '''

        :param user: the user that insert to db,
        user structure {name}
        :return:
        '''
        #TODO INSERT USER INGO DB
        pass

    def verify_password(self,username,password):
        # todo verify user's password
        pass

    def update(self,user):
        '''
        update user
        :param user:
        :return:user
        '''
        # todo update user

