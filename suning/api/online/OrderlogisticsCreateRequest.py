# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderlogisticsCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.expressCompanyName = None
        self.expressOrderId = None
        self.logisticsCode = None
        self.operateType = None
        self.orderId = None
        self.orderItemId = None
        self.reOrderItemId = None
        self.sheetId = None
        self.skuId = None
        
        self.setParamRule({
        	'expressCompanyName':{'allow_empty':False},
        	'expressOrderId':{'allow_empty':False},
        	'logisticsCode':{'allow_empty':False},
        	'operateType':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'reOrderItemId':{'allow_empty':False},
        	'sheetId':{'allow_empty':False},
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createOrderlogistics'

    def getApiMethod(self):

        return 'suning.online.orderlogistics.create'



