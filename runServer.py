#coding=utf-8
from flask import Flask
from flask_restful import Api
# from .registerView import Register
from registerView import Register

app = Flask(__name__)
api = Api(app)

# register 'Register' Resource
api.add_resource(Register,'/register',endpoint='register')


if __name__ == '__main__':
    app.run(debug=True)





