#!/usr/bin/env python
#-*-coding:utf-8-*-

##定义蓝图
from flask import Blueprint

adminbapp = Blueprint("admin",__name__)         #adminbapp为蓝图的名称

import admin.views