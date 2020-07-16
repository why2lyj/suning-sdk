# -*- coding: utf-8 -*-

'''

Created on 2018-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemIds = None
        self.supplierCode = None
        
        self.setParamRule({
        	'orderItemIds':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addOrder'

    def getApiMethod(self):

        return 'suning.selfmarket.order.add'



