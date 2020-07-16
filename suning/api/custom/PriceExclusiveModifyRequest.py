# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceExclusiveModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.createWay = None
        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.channelInfo = None
        self.priceType = None
        self.productList = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyPriceExclusive'

    def getApiMethod(self):

        return 'suning.custom.priceexclusive.modify'



