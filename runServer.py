# coding=utf-8

from flask import Flask
from flask_restful import Api
# from .registerView import Register
from registerView import RegisterView
from userView import UserView
from loginView import LoginView
from devicesAuditView import DeviceAuditView

app = Flask(__name__)
app.config.from_pyfile('config.py')

api = Api(app)

# register 'Register' Resource
api.add_resource(RegisterView,'/register',endpoint='register')
api.add_resource(UserView,'/user','/user/<user_id>',endpoint='user')
api.add_resource(LoginView,'/login','/logout',endpoint='login_logout')
api.add_resource(DeviceAuditView,'/deviceAudit','/deviceAudit/<audit_id>',endpoint='deviceAudit')

if __name__ == '__main__':
    app.run(debug=True)





