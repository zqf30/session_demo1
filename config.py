# encoding:utf-8
import os

# mysql+mysqlconnector://账号:密码@localhost/appname
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = 'zqf666'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo2'
SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT
                                                          , DRIVER
                                                          , USERNAME
                                                          , PASSWORD
                                                          , HOST
                                                          , PORT
                                                          , DATABASE
                                                          )
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False

