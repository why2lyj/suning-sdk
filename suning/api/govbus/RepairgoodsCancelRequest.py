# -*- coding: utf-8 -*-

'''

Created on 2019-6-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class RepairgoodsCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cancelReason = None
        self.orderId = None
        self.orderItemId = None
        self.sheetId = None
        self.skuId = None
        
        self.setParamRule({
        	'cancelReason':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'sheetId':{'allow_empty':False},
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelRepairgoods'

    def getApiMethod(self):

        return 'suning.govbus.repairgoods.cancel'



