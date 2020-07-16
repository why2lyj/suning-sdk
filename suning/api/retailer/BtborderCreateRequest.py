# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.orderDelivery = None
        self.orderInvoice = None
        self.orderItemList = None
        self.outerOrderNo = None
        self.payWay = None
        self.remark = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createBtborder'

    def getApiMethod(self):

        return 'suning.retailer.btborder.create'



