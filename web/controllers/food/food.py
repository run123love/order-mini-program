# -*- coding:utf-8 -*-
from flask import Blueprint, render_template


# 定义一个route_food蓝图，用来管理fodd_page路由
route_food = Blueprint("food_page", __name__)


@route_food.route("/index")
def index():
    return render_template("/food/info.html")


@route_food.route("/cat")
def cat():
    return render_template("/food/cat.html")


@route_food.route("/cat-set")
def cat_set():
    return render_template("food/cat_set.html")


@route_food.route("/info")
def info():
    return render_template("/food/info.html")


@route_food.route("/set")
def set_():
    return render_template("/food/set.html")
