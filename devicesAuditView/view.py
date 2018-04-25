# -*- coding: utf-8 -*-
from flask import Flask,make_response,jsonify,session,request
from flask_restful import Resource,Api,reqparse
# from ..models import UserModel
from models import UserModel
from commoon import verify_token

class DeviceAuditView(Resource):


    def get(self):
        '''
        get details info of a device audit
        :return:
        '''
        pass

    def post(self):
        '''
        change audit status
        :return:
        '''
        pass

    def delete(self):
        '''
        delete a device audit
        :return:
        '''
        pass

    def put(self):
        '''
        add a device audit
        :return:
        '''



