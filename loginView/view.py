# -*- coding: utf-8 -*-
from flask import Flask,make_response,jsonify,session,request
from flask_restful import Resource,Api,reqparse
# from ..models import UserModel
from models import UserModel
from commoon import verify_token

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,location='json',required=True)
parser.add_argument('password',type=str,location='json',required=True)


class LoginView(Resource):

        def post(self):
            '''
            login
            :return:
            '''
            userModel = UserModel()
            register_data = parser.parse_args()
            name = register_data['name']
            password = register_data['password']
            user = userModel.getUser(username=name)
            if user and user['password'] == password:
                session['user'] = name
                response = make_response(jsonify({'code':200,'msg':u'登录成功'}))
                response.set_cookie("token",name)
                response.headers['Content-Type'] = 'application/json'
                # response.headers['Set-Cookie'] = 'token=songyue; Path=/'
                return response
            else:
                return {"code":1003,"error":u'用户名密码不正确!'},400

        @verify_token
        def get(self):
            '''
            logout
            :return:
            '''
            user_session = session.pop('user',None)
            response = make_response(jsonify({'code':200,'msg':u'退出登录成功!'}))
            response.delete_cookie('token')
            response.headers['Content-Type'] = 'application/json'
            return response







