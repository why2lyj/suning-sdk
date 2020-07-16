# -*- coding: utf-8 -*-

'''

Created on 2020-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderbysupplymodeCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.creator = None
        self.orderDelivery = None
        self.orderItems = None
        self.remark = None
        self.storeCode = None
        self.submitType = None
        self.supplyMode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'creator':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'submitType':{'allow_empty':False},
        	'supplyMode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createBtborderbysupplymode'

    def getApiMethod(self):

        return 'suning.retailer.btborderbysupplymode.create'



