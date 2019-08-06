# -*- coding:utf-8 -*-
# =================
# 在个文件中管理我们app的入口
# =================
from application import app, manager
from flask_script import Server
import traceback
import www

# 自定义runserver命令
manager.add_command("runserver",
                    Server(app.config.get("SERVER_IP", "0.0.0.0"),
                           port=app.config.get("SERVER_PORT", "5000"),
                           use_debugger=True, use_reloader=True))


if __name__ == '__main__':
    try:
        manager.run()
    except Exception as e:
        traceback.print_exc()
