# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class GuacouponCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.activityPattern = None
        self.activityTimesLimit = None
        self.assignedRole = None
        self.couponType = None
        self.endTime = None
        self.peopleActivityTimesLimit = None
        self.productScope = None
        self.rewardAmount = None
        self.shopCode = None
        self.showRegion = None
        self.startTime = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'activityPattern':{'allow_empty':False},
        	'activityTimesLimit':{'allow_empty':False},
        	'assignedRole':{'allow_empty':False},
        	'couponType':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'peopleActivityTimesLimit':{'allow_empty':False},
        	'productScope':{'allow_empty':False},
        	'rewardAmount':{'allow_empty':False},
        	'shopCode':{'allow_empty':False},
        	'showRegion':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createGuacoupon'

    def getApiMethod(self):

        return 'suning.custom.guacoupon.create'



