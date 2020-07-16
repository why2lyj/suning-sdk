# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderdiscountsideCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.allShopType = None
        self.appStoreCode = None
        self.baseQuantifierType = None
        self.channelInfo = None
        self.endTime = None
        self.productList = None
        self.rewardQuantifierType = None
        self.ruleList = None
        self.startTime = None
        self.storeCode = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'allShopType':{'allow_empty':False},
        	'baseQuantifierType':{'allow_empty':False},
        	'channelInfo':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'rewardQuantifierType':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createOrderdiscountside'

    def getApiMethod(self):

        return 'suning.store.orderdiscount.create'



