# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplyreturngoodsCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyType = None
        self.attachInfo = None
        self.orderId = None
        self.orderItemId = None
        self.orderStatus = None
        self.packInfo = None
        self.picInfo = None
        self.reOrderItemId = None
        self.retDesc = None
        self.retNum = None
        self.retReason = None
        self.useInfo = None
        
        self.setParamRule({
        	'applyType':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'orderStatus':{'allow_empty':False},
        	'reOrderItemId':{'allow_empty':False},
        	'retReason':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createApplyreturngoods'

    def getApiMethod(self):

        return 'suning.online.applyreturngoods.create'



