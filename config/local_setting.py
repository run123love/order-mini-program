# -*- utf-8 -*-
# =======================
# 这个文件配置本地开发的配置
# =======================

SERVER_IP = "127.0.0.1"  # 0.0.0.0因为vpn给禁了，所以用127.0.0.1
SERVER_PORT = 8889
ENV = "development"
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:lhs123king@localhost/mysql"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = "utf-8"
