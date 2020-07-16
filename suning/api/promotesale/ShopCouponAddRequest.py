# -*- coding: utf-8 -*-

'''

Created on 2015-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopCouponAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.activityPattern = None
        self.showRegion = None
        self.activityTimesLimit = None
        self.assignedRole = None
        self.rewardAmount = None
        self.couponType = None
        self.baseAmount = None
        self.peopleActivityTimesLimit = None
        self.effectStartTime = None
        self.effectEndTime = None
        self.channelInfo = None
        self.productRange = None
        self.productList = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'activityPattern':{'allow_empty':False},
        	'showRegion':{'allow_empty':False},
        	'activityTimesLimit':{'allow_empty':False},
        	'assignedRole':{'allow_empty':False},
        	'rewardAmount':{'allow_empty':False},
        	'couponType':{'allow_empty':False},
        	'baseAmount':{'allow_empty':False},
        	'peopleActivityTimesLimit':{'allow_empty':False},
        	'effectStartTime':{'allow_empty':False},
        	'effectEndTime':{'allow_empty':False},
        	'channelInfo':{'allow_empty':False},
        	'productRange':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addShopCoupon'

    def getApiMethod(self):

        return 'suning.custom.shopcoupon.add'



