# -*- coding: utf-8 -*-

'''

Created on 2020-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReturngoodsCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.operateType = None
        self.orderId = None
        self.orderItemId = None
        self.reOrderItemId = None
        self.skuId = None
        
        self.setParamRule({
        	'operateType':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'reOrderItemId':{'allow_empty':False},
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelReturngoods'

    def getApiMethod(self):

        return 'suning.online.returngoods.cancel'



