# -*- coding: utf-8 -*-

'''

Created on 2019-1-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class FreevoucherCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.activitySecretKey = None
        self.chanId = None
        self.city = None
        self.couponAmount = None
        self.couponGetSource = None
        self.memberNo = None
        self.mobileNum = None
        self.operateType = None
        self.orderId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'activitySecretKey':{'allow_empty':False},
        	'chanId':{'allow_empty':False},
        	'couponGetSource':{'allow_empty':False},
        	'mobileNum':{'allow_empty':False},
        	'operateType':{'allow_empty':False},
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createFreevoucher'

    def getApiMethod(self):

        return 'suning.online.freevoucher.create'



