# -*- coding:utf-8 -*-
# =================
# 在个文件中封装我们的app
# =================
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from loguru import logger


class Application(Flask):
    """封装一个Flask app

    实现配置分离

    :param import_name: the name of the application package
    """
    def __init__(self, import_name: str,
                 temp_folder: str = None,
                 root_path=None,
                 static_folder=None):
        super().__init__(import_name,
                         template_folder=temp_folder,
                         root_path=root_path,
                         static_folder=static_folder)
        self.__config_when_env()
        db.init_app(self)

    def __config_when_env(self):
        """通过环境变量加载app配置"""
        logger.debug("开始配置app......")
        name_of_config_env = os.environ.get("ops_config", "base")
        self.config.from_pyfile(f"config/{name_of_config_env}_setting.py")
        logger.debug("app配置成功，当前采用的配置为：{}", name_of_config_env)


db = SQLAlchemy()
app = Application(__name__,
                  temp_folder=os.getcwd() + "/web/templates",
                  root_path=os.getcwd())
manager = Manager(app)

# 注入模板方法
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildUrl, "buildUrl")
app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")


