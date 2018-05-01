# -*- coding: utf-8 -*-
from flask import Flask,make_response,jsonify,session,request
from flask_restful import Resource,Api,reqparse
from models import DeviceAuditModel
from commoon import verify_token,isAdministrator,AUDIT_SAVE,AUDIT_PENDING,AUDIT_COMPLETE

parse = reqparse.RequestParser()
parse.add_argument('deviceName',type=unicode,location='json',required=True)
parse.add_argument('deviceModel',type=unicode,location='json',required=True)
parse.add_argument('price',type=unicode,location='json',required=True)
parse.add_argument('buyer',type=unicode,location='json',required=True)
parse.add_argument('applyDate',type=unicode,location='json',required=True)
parse.add_argument('action',type=int,location='json',choices=(1,2),required=True)

class DeviceAuditView(Resource):
    '''
    device audit fields:
    deviceName,deviceModel,price、buyer、applyDate
    '''
    method_decorators = verify_token

    def get(self,audit_id='all'):
        '''
        get details info of a device audit
        :return:
        '''
        user = session['currentUser']
        deviceAuditModel = DeviceAuditModel()

        if user != 'admin':
            query_re = deviceAuditModel.getAuditInfoByUser(user)
        else:
            query_re = deviceAuditModel.getAllAuditInfo()
        return {'code':200,'msg':u'获取设备申请信息成功','total':len(query_re),'data':query_re}

    def post(self,audit_id):
        '''
        change audit status
        :return:
        '''
        data = parse.parse_args()
        deviceName = data['deviceName']
        deviceModel = data['deviceModel']
        price = data['price']
        buyer = data['buyer']
        applyDate = data['applyDate']
        action = data['action']
        deviceAuditInfo = {'deviceName': deviceName, 'deviceModel': deviceModel,
                           'price': price, 'buyer': buyer, 'applyDate': applyDate,
                           'action': action}

        user = session['currentUser']
        deviceAuditModel = DeviceAuditModel()
        query_status = deviceAuditModel.getDeviceAuditInfo(audit_id)
        if query_status['action'] == AUDIT_SAVE:
            if action == AUDIT_COMPLETE:
                return {'code': 1011, 'error': u'修改设备申请信息失败,该审核信息还未提交'}, 400

        if query_status['action'] != AUDIT_PENDING:
            if action == AUDIT_PENDING:
                return {'code':1012,'error':u'修改设备申请信息失败,该审核信息已提交并处于审核中状态'},400

        if action == AUDIT_COMPLETE:
            if action == AUDIT_PENDING or action == AUDIT_PENDING:
                return {'code':1013,'error':u'修改设备申请信息失败,该审核信息已审核完成'}

        if user == query_status['buyer'] or user == 'admin':
            update_re = deviceAuditModel.update(audit_id,deviceAuditInfo)
            if update_re:
                return {'code': 200, 'msg': u'修改设备申请信息成功,audit_id=%s' % audit_id,'data':deviceAuditInfo}
            else:
                return {'code': 1014, 'error': u'修改设备申请信息失败,audit_id=%s' % audit_id}, 400
        return {'code':1015,'error':u'对不起,你没有修改该申请信息的权限'}

    def delete(self,audit_id):
        '''
        delete a device audit,if the status of audit is pending ,should not be deleted
        :return:
        '''
        user = session['currentUser']
        deviceAuditModel = DeviceAuditModel()

        query_status = deviceAuditModel.getDeviceAuditInfo(audit_id)
        if query_status['action'] != AUDIT_SAVE:
            return {'code':1010,'error':u'删除设备申请信息失败,此状态不允许删除'},400

        if user == query_status['buyer'] or user == 'admin':
            delete_re = deviceAuditModel.deleteDeviceAuditInfo(audit_id)
            if delete_re:
                return {'code': 200, 'msg': u'删除设备申请信息成功,audit_id=%s' % audit_id}
            else:
                return {'code': 1008, 'error': u'删除设备申请信息失败,audit_id=%s' % audit_id}, 400
        return {'code':1011,'error':u'对不起,你没有删除该申请信息的权限'}

    def put(self):
        '''
        add a device audit
        :return:
        '''
        data = parse.parse_args()
        deviceName = data['deviceName']
        deviceModel = data['deviceModel']
        price = data['price']
        buyer = data['buyer']
        applyDate = data['applyDate']
        action = data['action']
        if action == AUDIT_COMPLETE:
            return {'code':1009,'error':u'添加设备申请状态不正确,action=%s'%action}

        deviceAuditInfo = {'deviceName': deviceName, 'deviceModel': deviceModel,
                           'price': price, 'buyer': buyer, 'applyDate': applyDate,
                           'action':action}

        tmp_deviceAuditInfo = deviceAuditInfo.copy()
        deviceAuditModel = DeviceAuditModel()
        try:
            insert_id = deviceAuditModel.insert(deviceAuditInfo)
            tmp_deviceAuditInfo.update(id=insert_id)
            return {'code':200,'msg':u'添加设备申请信息成功','data':tmp_deviceAuditInfo}
        except:
            return {'code':1007,'error':u'添加设备信息失败'},400


