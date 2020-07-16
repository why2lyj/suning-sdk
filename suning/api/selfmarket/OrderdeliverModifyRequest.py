# -*- coding: utf-8 -*-

'''

Created on 2019-10-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderdeliverModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.expressCompCode = None
        self.expressNo = None
        self.orderItemId = None
        self.supplierCode = None
        
        self.setParamRule({
        	'expressCompCode':{'allow_empty':False},
        	'expressNo':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyOrderdeliver'

    def getApiMethod(self):

        return 'suning.selfmarket.orderdeliver.modify'



