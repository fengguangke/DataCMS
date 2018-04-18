# coding=utf-8

from models import UserModel
from flask_restful import Resource,reqparse
from models import UserModel

parse = reqparse.RequestParser()
parse.add_argument('username',type=str,location='json',required=False)
parse.add_argument('age',type=int,location='json',required=False)
parse.add_argument('sex',type=str,location='json',required=False)
parse.add_argument('phone',type=str,location='json',required=False)
parse.add_argument('address',type=str,location='json',required=False)
parse.add_argument('email',type=str,location='json',required=False)
parse.add_argument('qq',type=str,location='json',required=False)
parse.add_argument('avatar',type=str,location='json',required=False)

class UserView(Resource):
    # todo add api auth

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
        :param user_id:
        :return:user
        '''
        # todo update user
        update_data = parse.parse_args()
        pass

    def delete(self,user_id):
        '''
        delete user by user_id
        :param user_id:
        :return:
        '''
        pass
        # todo





