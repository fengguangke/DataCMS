from pymongo import MongoClient


class User():

    def getUser(self,username):
        '''
        get user from mongodb by username
        :param username:
        :return:
        '''
        user = {'name':'fengguangke',
                'password':'xx'}
        return user
