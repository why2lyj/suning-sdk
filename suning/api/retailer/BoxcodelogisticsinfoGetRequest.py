# -*- coding: utf-8 -*-

'''

Created on 2020-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class BoxcodelogisticsinfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.boxCode = None
        self.orderNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'boxCode':{'allow_empty':False},
        	'orderNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getBoxcodelogisticsinfo'

    def getApiMethod(self):

        return 'suning.retailer.boxcodelogisticsinfo.get'



