# coding=utf-8

from flask_restful import Resource,reqparse
from flask import jsonify,session

parse_header = reqparse.RequestParser()
parse_header.add_argument('token',type=str,location='headers',required=True,help=u'token认证信息错误')

def verify_token(fun):
    def wrapper(*args,**kwargs):
        token = parse_header.parse_args()['token']
        # if not token:
        #     return jsonify({'code':4001,'error':u'缺少认证信息token'}),401
        if 'user' in session:
            if token != session['user']:
                return jsonify({'code':4002,'error':u'token认证信息错误'})
            return fun(*args,**kwargs)
        return jsonify({'code':500,'error':u'服务器错误,session["user"]不存在，请登录'})
    return wrapper

def isAdministrator(fun):
    def wrapper(*args,**kwargs):
        token = parse_header.parse_args()['token']
        if 'user' in session:
            if token != session['user']:
                return jsonify({'code': 4002, 'error': u'token认证信息错误'})
            if token != 'admin':
                return jsonify({"code": 4003, 'error': u"对不起，您没有此权限!"})
            return fun(*args,**kwargs)
        return jsonify({'code': 500, 'error': u'服务器错误,session["user"]不存在，请登录'})
    return wrapper