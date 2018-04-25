# coding=utf-8

from pymongo import MongoClient
from bson import ObjectId
from flask import current_app

class DeviceAuditModel():

    def __init__(self,*args,**kwargs):
        collection = 'CMSData_deviceAudit'
        mongo_url = current_app.config['MONGO_URL']
        mongo = MongoClient(mongo_url)
        db = mongo.get_database(current_app.config['MONGO_DB'])
        self.collection = db.get_collection(collection)

    def insert(self):
        '''

        :return:
        '''
        pass

    def getDeviceAuditInfo(self):
        '''

        :return:
        '''
        pass

    def deleteDeviceAuditInfo(self):
        '''

        :return:
        '''
        pass

    def update(self):
        '''

        :return:
        '''
        pass

    def changeAuditStatus(self):
        '''

        :return:
        '''
        pass