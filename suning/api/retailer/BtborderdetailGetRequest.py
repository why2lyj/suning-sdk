# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderdetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.orderItemNo = None
        self.orderNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'orderNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getBtborderdetail'

    def getApiMethod(self):

        return 'suning.retailer.btborderdetail.get'



