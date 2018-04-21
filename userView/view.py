# coding=utf-8

from flask import jsonify,request,session
from flask_restful import Resource,reqparse
from models import UserModel
from commoon import verify_token

parse = reqparse.RequestParser()
parse.add_argument('username',type=str,location='json',required=False)
parse.add_argument('realName',type=unicode,location='json',required=False)
parse.add_argument('age',type=int,location='json',required=False)
parse.add_argument('sex',type=unicode,location='json',required=False)
parse.add_argument('phone',type=str,location='json',required=False)
parse.add_argument('address',type=unicode,location='json',required=False)
parse.add_argument('email',type=unicode,location='json',required=False)
parse.add_argument('qq',type=str,location='json',required=False)
parse.add_argument('avatar',type=unicode,location='json',required=False)

parse_header = reqparse.RequestParser()
parse.add_argument('token',type=str,location='headers',required=True)

class UserView(Resource):

    method_decorators = [verify_token]

    def get(self,user_id):
        '''
        get user info by user_id
        :param user_id:
        :return: user
        '''
        userModel = UserModel()
        user = userModel.getUserById(user_id)
        if user:
            return {'code':200,'msg':u'获取用户信息成功','user':user}
        else:
            return {'code':1002,'error':u'获取用户信息失败'},400

    def post(self,user_id):
        '''
        update user by user_id
        '''
        update_data = parse.parse_args()
        name = update_data['username']
        realName = update_data['realName']
        age = update_data['age']
        sex = update_data['sex']
        phone = update_data['phone']
        address = update_data['address']
        email = update_data['email']
        qq = update_data['qq']
        avatar = update_data['avatar']
        user = {'username':name,'realName':realName,'age':age,'sex':sex,'phone':phone,
                'address':address,'email':email,'qq':qq,'avatar':avatar
                }

        userModel = UserModel()
        update_re = userModel.update(user_id=user_id,user_info=user)
        if update_re:
            return {'code':200,'msg':u'更新用户信息成功：user_id=%s'%user_id}
        else:
            return {'code':1005,'error':u"更新用户信息失败: user_id=%s"%user_id},400

    def delete(self,user_id):
        '''
        delete user by user_id
        :param user_id:
        :return:
        '''
        userModel = UserModel()
        delete_re = userModel.deleteUserById(user_id)
        if delete_re:
            return {'code':200,'msg':u'删除用户成功,user_id=%s'%user_id}
        else:
            return {'code':1006,'error':u'删除用户信息失败,user_id=%s'%user_id},400



