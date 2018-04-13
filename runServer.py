# coding=utf-8

from flask import Flask
from flask_restful import Api
# from .registerView import Register
from registerView import RegisterView
from userView import UserView

app = Flask(__name__)
api = Api(app)

# register 'Register' Resource
api.add_resource(RegisterView,'/register',endpoint='register')
api.add_resource(UserView,'/user','/user/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)





