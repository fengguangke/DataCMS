from flask import Flask
from flask_restful import Resource,Api,reqparse
from ..models.user import User

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name',type='str',location='json',required=True)
parser.add_argument('password',type='str',location='json',required=True)


class Register(Resource):

        def post(self):
            register_data = parser.parse_args()
            name = register_data['name']
            password = register_data['password']
