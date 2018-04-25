# coding=utf-8

from flask import Flask
from flask_restful import Api
# from .registerView import Register
from registerView import RegisterView
from userView import UserView
from loginView import LoginView

app = Flask(__name__)
app.config.from_pyfile('config.py')

api = Api(app)

# register 'Register' Resource
api.add_resource(RegisterView,'/register',endpoint='register')
api.add_resource(UserView,'/user','/user/<user_id_or_name>',endpoint='user')
api.add_resource(LoginView,'/login','/logout',endpoint='login_logout')


if __name__ == '__main__':
    app.run(debug=True)





