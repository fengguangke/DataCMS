# coding=utf-8

from flask import jsonify,request,session
from flask_restful import Resource,reqparse,fields
from models import UserModel
from commoon import verify_token,isAdministrator

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

parse_arg = reqparse.RequestParser()
parse_arg.add_argument('type',type=str,location='args',choices=('name','id'),required=True)
parse_arg.add_argument('value',type=str,location='args',required=True)

class UserView(Resource):

    # method_decorators = [verify_token]
    @verify_token
    def get(self):
        '''
        get user info by user_id
        :param user_id:
        :return: user
        '''
        userModel = UserModel()

        type_value = parse_arg.parse_args()
        type = type_value['type']
        user_id_or_name = type_value['value']
        if type == 'name':
            user_id = userModel.getUserIdByName(user_id_or_name)
            if user_id:
                return {'code': 200, 'msg': u'获取用户id成功', 'user_id': user_id}
            else:
                return {'code': 1004, 'error': u'获取用户id成功失败'}, 400
        else:
            user = userModel.getUserById(user_id_or_name)
            user['id'] = user_id_or_name
            if user:
                return {'code': 200, 'msg': u'获取用户信息成功', 'user': user}
            else:
                return {'code': 1002, 'error': u'获取用户信息失败'}, 400

    @verify_token
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

    @isAdministrator
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



