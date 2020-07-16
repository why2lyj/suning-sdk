# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SsshopcouponAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityEndTime = None
        self.activityName = None
        self.activityStartTime = None
        self.appStoreCode = None
        self.baseAmount = None
        self.baseQuantifierType = None
        self.circulation = None
        self.couponType = None
        self.denomination = None
        self.dynamicDistanceTimeDelay = None
        self.dynamicTime = None
        self.effectiveEndTime = None
        self.effectiveStartTime = None
        self.grantCountEveryday = None
        self.limitCollarCount = None
        self.limitCollarEveyDay = None
        self.shopCode = None
        self.showRegion = None
        self.useChannelStr = None
        self.validityType = None
        self.voucheObject = None
        
        self.setParamRule({
        	'activityEndTime':{'allow_empty':False},
        	'activityName':{'allow_empty':False},
        	'activityStartTime':{'allow_empty':False},
        	'baseAmount':{'allow_empty':False},
        	'baseQuantifierType':{'allow_empty':False},
        	'circulation':{'allow_empty':False},
        	'couponType':{'allow_empty':False},
        	'denomination':{'allow_empty':False},
        	'effectiveEndTime':{'allow_empty':False},
        	'effectiveStartTime':{'allow_empty':False},
        	'limitCollarCount':{'allow_empty':False},
        	'limitCollarEveyDay':{'allow_empty':False},
        	'showRegion':{'allow_empty':False},
        	'useChannelStr':{'allow_empty':False},
        	'validityType':{'allow_empty':False},
        	'voucheObject':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSsshopcoupon'

    def getApiMethod(self):

        return 'suning.store.ssshopcoupon.add'



