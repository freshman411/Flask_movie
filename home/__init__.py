#!/usr/bin/env python
#-*-coding:utf-8-*-

##定义蓝图

from flask import Blueprint

homebapp = Blueprint("home",__name__)

import home.views