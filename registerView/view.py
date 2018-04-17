#coding=utf-8

from flask_restful import Resource,reqparse
# from ..models import UserModel
from models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,location='json',required=True)
parser.add_argument('password',type=str,location='json',required=True)


class RegisterView(Resource):

        def post(self):
            userModel = UserModel()
            register_data = parser.parse_args()
            name = register_data['name']
            password = register_data['password']
            user = userModel.getUser(username=name)
            if not user:
                userMap = dict(username=name,password=password,realname='',age=0,sex='',phone='',address='',email='',qq='',avatar='')
                user = userMap.copy()
                userModel.insert(userMap)
                return {'code':200,'msg':u'注册用户成功','user':user}
            else:
                return {'code':'1001','error':u'用户名已存在'},400

