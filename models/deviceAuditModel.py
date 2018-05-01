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

    def getAllAuditInfo(self):
        result_cur = self.collection.find()
        result = list(result_cur)
        map_result = map(lambda d: d.update({'_id', str('_id')}), result)
        return map_result

    def getAuditInfoByUser(self,userName):
        '''
        :param userName: string object like "'luffy','baobao'"
        :return:
        '''
        result_cur = self.collection.find({'buyer':userName})
        result = list(result_cur)
        map_result = map(lambda d:d.update({'_id',str('_id')}),result)
        return map_result

    def insert(self,deviceAuditInfo):
        '''
        :return:
        '''
        result = self.collection.insert_one(deviceAuditInfo)
        return str(result.inserted_id)

    def getDeviceAuditInfo(self,audit_id):
        '''

        :return:
        '''
        result = self.collection.find_one({'_id':ObjectId(audit_id)},projection={'_id': False})
        return result

    def deleteDeviceAuditInfo(self,audit_id):
        '''
        :return:
        '''
        result = self.collection.find_one_and_delete({'_id': ObjectId(audit_id)})
        if result:
            return True
        return False

    def update(self,audit_id,audit_info):
        '''
        :return:
        '''
        result = self.collection.find_one_and_update({'_id': ObjectId(audit_id)},
                                                     {"$set": {'deviceName': audit_info['deviceName'],
                                                               'deviceModel': audit_info['deviceModel'],
                                                               'price': audit_info['price'],
                                                               'buyer': audit_info['buyer'],
                                                               'applyDate': audit_info['applyDate'],
                                                               'action':audit_info['action']
                                                               }})
        if result:
            return True
        return False

    def changeAuditStatus(self,audit_id):
        '''

        :return:
        '''
