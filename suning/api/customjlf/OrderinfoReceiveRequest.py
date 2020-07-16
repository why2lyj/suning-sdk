# -*- coding: utf-8 -*-

'''

Created on 2019-10-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderinfoReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cfOrderId = None
        self.orderDate = None
        self.orderTime = None
        self.orderSource = None
        self.salePlatform = None
        self.orderChannel = None
        self.orderMemo = None
        self.orderItemQty = None
        self.cfTradePays = None
        self.payItemQty = None
        self.orderSaleTotalAmt = None
        self.realPayAmt = None
        self.totalSrvFee = None
        self.totalTax = None
        self.totalShippingFee = None
        self.orderSerialNumber = None
        self.cfOrders = None
        
        self.setParamRule({
        	'cfOrderId':{'allow_empty':False},
        	'orderDate':{'allow_empty':False},
        	'orderTime':{'allow_empty':False},
        	'orderSource':{'allow_empty':False},
        	'salePlatform':{'allow_empty':False},
        	'orderChannel':{'allow_empty':False},
        	'orderItemQty':{'allow_empty':False},
        	'payItemQty':{'allow_empty':False},
        	'orderSaleTotalAmt':{'allow_empty':False},
        	'realPayAmt':{'allow_empty':False},
        	'orderSerialNumber':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiveOrderinfo'

    def getApiMethod(self):

        return 'suning.customjlf.orderinfo.receive'



