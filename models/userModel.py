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
        collection = 'CMSData_user'
        mongo_url = current_app.config['MONGO_URL']
        mongo = MongoClient(mongo_url)
        db = mongo.get_database(current_app.config['MONGO_DB'])
        self.collection = db.get_collection(collection)

    def getUserById(self,user_id):

        user = self.collection.find_one({"_id":user_id},projection={'_id': False})
        return user

    def getUser(self,username):
        '''
        get user from mongodb by username
        :param username:
        :return:
        '''
        user = self.collection.find_one({'username':username})
        return user

    def insert(self,user):
        '''

        :param user: the user that insert to db,
        user structure {name}
        :return:
        '''
        self.collection.insert_one(user)

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

