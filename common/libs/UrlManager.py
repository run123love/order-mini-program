# -*- coding:utf-8 -*-

import time
from application import app


class UrlManager:

    @classmethod
    def buildUrl(cls, path: str):
        return path

    @classmethod
    def buildStaticUrl(cls, path: str):
        release_version = app.config.get('RELEASE_VERSION', int(time.time()))
        new_path = f"/static{path}?ver={release_version}"
        return UrlManager.buildUrl(new_path)
