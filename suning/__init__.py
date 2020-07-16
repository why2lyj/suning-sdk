# -*- coding: utf-8 -*-
"""
Created on 2014-05-21

@author: momo
"""
from suning.api.abstract import *
from suning.util import *


class appinfo(object):
    """
        包含appkey和appsecrect
    """

    def __init__(self, appkey, appsecrect):
        self.appkey = appkey
        self.appsecrect = appsecrect
def getDefaultAppInfo():
    pass


def setDefaultAppInfo(appkey, appsecrect):
    """
        设置默认的appkey和secret
    @param appkey: appkey
    @param appsecrect:  appsecrect
    """
    default = appinfo(appkey, appsecrect)
    global getDefaultAppInfo
    getDefaultAppInfo = lambda: default    