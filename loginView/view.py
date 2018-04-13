# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource,Api,reqparse
# from ..models import UserModel
from models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('name',type='str',location='json',required=True)
parser.add_argument('password',type='str',location='json',required=True)


class Login(Resource):

        def post(self):
            register_data = parser.parse_args()
            name = register_data['name']
            password = register_data['password']




