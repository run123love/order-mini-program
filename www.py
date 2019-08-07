# -*- coding:utf-8 -*-
from application import app
from web.controllers.index import route_index
from web.controllers.user.user import route_user
from web.controllers.static import route_static
from web.controllers.account.account import route_account
from web.controllers.member.member import route_member
from web.controllers.finance.finance import route_finance
from web.controllers.food.food import route_food
from web.controllers.stat.stat import route_stat


app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_account, url_prefix="/account")
app.register_blueprint(route_member, url_prefix="/member")
app.register_blueprint(route_finance, url_prefix="/finance")
app.register_blueprint(route_food, url_prefix="/food")
app.register_blueprint(route_stat, url_prefix="/stat")
