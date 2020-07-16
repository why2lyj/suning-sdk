# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReceivefreecouponCreateRequest(AbstractApi):

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
        self.operateType = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'activitySecretKey':{'allow_empty':False},
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'couponGetSource':{'allow_empty':False},
        	'memberNo':{'allow_empty':False},
        	'operateType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createReceivefreecoupon'

    def getApiMethod(self):

        return 'suning.online.receivefreecoupon.create'



