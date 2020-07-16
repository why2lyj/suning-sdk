# -*- coding: utf-8 -*-

'''

Created on 2019-10-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDeliverAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.expressCompCode = None
        self.expressNo = None
        self.orderItemId = None
        self.sender = None
        self.senderTel = None
        self.sign = None
        self.supplierCode = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addOrderDeliver'

    def getApiMethod(self):

        return 'suning.selfmarket.orderdeliver.add'



