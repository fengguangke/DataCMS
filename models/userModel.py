# coding=utf-8

from pymongo import MongoClient
from bson import ObjectId
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

        user = self.collection.find_one({"_id":ObjectId(user_id)},projection={'_id': False})
        return user

    def getUser(self, username):
        '''
        get user from mongodb by username
        :param username:
        :return:
        '''
        user = self.collection.find_one({'username': username})
        return user

    def getUserIdByName(self,username):
        '''
        get user from mongodb by username
        :param username:
        :return:
        '''
        user_Id = self.collection.find_one({'username':username},projection=['_id'])
        return str(user_Id['_id'])

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

    def update(self,user_id,user_info):
        '''
        update user
        :param user_id:
        :param user_info:
        :return:user
        '''

        result = self.collection.find_one_and_update({'_id':ObjectId(user_id)},
                                            {"$set":{'username':user_info['username'],
                                                     'realName':user_info['realName'],
                                                     'age':user_info['age'],
                                                     'sex':user_info['sex'],
                                                     'phone':user_info['phone'],
                                                     'address':user_info['address'],
                                                     'email':user_info['email'],
                                                     'qq':user_info['qq'],
                                                     'avatar':user_info['avatar']
                                                     }})
        if result:
            return True
        return False

    def deleteUserById(self,user_id):
        '''
        delete user bu user_id
        :return:
        '''

        result = self.collection.find_one_and_delete({'_id':ObjectId(user_id)})
        if result:
            return True
        return False