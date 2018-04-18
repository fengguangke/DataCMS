# -*- coding: utf-8 -*-
from flask import Flask,make_response,Response,jsonify
from flask_restful import Resource,Api,reqparse
# from ..models import UserModel
from models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,location='json',required=True)
parser.add_argument('password',type=str,location='json',required=True)


class LoginView(Resource):

        def post(self):
            userModel = UserModel()
            register_data = parser.parse_args()
            name = register_data['name']
            password = register_data['password']
            user = userModel.getUser(username=name)
            if user and user['password'] == password:
                response = make_response(jsonify({'code':200,'msg':u'登录成功'}))
                response.set_cookie("token",name)
                response.headers['Content-Type'] = 'application/json'
                # response.headers['Set-Cookie'] = 'token=songyue; Path=/'
                return response
            else:
                return {"code":1003,"error":u'用户名密码不正确!'},400






