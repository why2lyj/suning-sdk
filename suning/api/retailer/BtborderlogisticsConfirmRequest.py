# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderlogisticsConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.orderItemNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'orderItemNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'confirmBtborderlogistics'

    def getApiMethod(self):

        return 'suning.retailer.btborderlogistics.confirm'



