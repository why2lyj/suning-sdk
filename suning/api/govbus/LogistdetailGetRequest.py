# -*- coding: utf-8 -*-

'''

Created on 2019-1-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogistdetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItemIds = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getLogistdetail'

    def getApiMethod(self):

        return 'suning.govbus.logistdetail.get'



