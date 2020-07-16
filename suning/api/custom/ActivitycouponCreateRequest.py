# -*- coding: utf-8 -*-

'''

Created on 2018-9-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivitycouponCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.activityTimesLimit = None
        self.assignedRole = None
        self.baseAmount = None
        self.couponType = None
        self.effectEndTime = None
        self.effectStartTime = None
        self.endTime = None
        self.rewardAmount = None
        self.shopCode = None
        self.startTime = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'activityTimesLimit':{'allow_empty':False},
        	'assignedRole':{'allow_empty':False},
        	'baseAmount':{'allow_empty':False},
        	'couponType':{'allow_empty':False},
        	'effectEndTime':{'allow_empty':False},
        	'effectStartTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'rewardAmount':{'allow_empty':False},
        	'shopCode':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createActivitycoupon'

    def getApiMethod(self):

        return 'suning.custom.activitycoupon.create'



