# -*- coding:utf-8 -*-

from flask import Blueprint, send_from_directory
from application import app
from loguru import logger


route_static = Blueprint("static", __name__)


@route_static.route("/<path:filename>")
def index(filename):
    #logger.debug(f"app.root_path: {app.root_path}")
    static_dir = app.root_path + "/web/static"
    #logger.info(f"静态文件夹地址为：{static_dir}")
    return send_from_directory(
        static_dir,
        filename=filename
    )
