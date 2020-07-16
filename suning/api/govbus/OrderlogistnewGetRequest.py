# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderlogistnewGetRequest(AbstractApi):

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

        return 'getOrderlogistnew'

    def getApiMethod(self):

        return 'suning.govbus.orderlogistnew.get'



