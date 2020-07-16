# -*- coding: utf-8 -*-

'''

Created on 2016-6-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderCouponAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.channelInfo = None
        self.activityProductType = None
        self.couponProductType = None
        self.returnCouponType = None
        self.returnCouponValue = None
        self.activityLimit = None
        self.activityTimesLimit = None
        self.peopleActivityTimesLimit = None
        self.effectDays = None
        self.baseQuantifierType = None
        self.rewardType = None
        self.areaCode = None
        self.booleanCap = None
        self.rewardList = None
        self.couponProductList = None
        self.activityProductList = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'channelInfo':{'allow_empty':False},
        	'activityProductType':{'allow_empty':False},
        	'couponProductType':{'allow_empty':False},
        	'returnCouponType':{'allow_empty':False},
        	'baseQuantifierType':{'allow_empty':False},
        	'rewardType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addOrderCoupon'

    def getApiMethod(self):

        return 'suning.custom.ordercoupon.add'



