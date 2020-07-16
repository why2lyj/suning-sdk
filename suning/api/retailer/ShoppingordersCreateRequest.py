# -*- coding: utf-8 -*-

'''

Created on 2018-8-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShoppingordersCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.buyerName = None
        self.buyerPhone = None
        self.createCode = None
        self.discountAmount = None
        self.discountCode = None
        self.installDelivery = None
        self.merchantCustNo = None
        self.orderAmount = None
        self.orderDelivery = None
        self.orderFrom = None
        self.orderItem = None
        self.outerOrderNo = None
        self.payAmount = None
        self.posCode = None
        self.remark = None
        self.salesMode = None
        self.storeCode = None
        self.userCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'buyerPhone':{'allow_empty':False},
        	'discountAmount':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'orderAmount':{'allow_empty':False},
        	'orderFrom':{'allow_empty':False},
        	'outerOrderNo':{'allow_empty':False},
        	'payAmount':{'allow_empty':False},
        	'salesMode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createShoppingorders'

    def getApiMethod(self):

        return 'suning.retailer.shoppingorders.create'



