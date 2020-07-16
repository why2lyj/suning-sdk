# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceExclusiveAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.createWay = None
        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.channelInfo = None
        self.priceType = None
        self.limitNum = None
        self.productList = None
        
        self.setParamRule({
        	'createWay':{'allow_empty':False},
        	'activityName':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'channelInfo':{'allow_empty':False},
        	'priceType':{'allow_empty':False},
        	'limitNum':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addPriceExclusive'

    def getApiMethod(self):

        return 'suning.custom.priceexclusive.add'



