# -*- coding: utf-8 -*-

'''

Created on 2017-4-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class PushOrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.buyerNick = None
        self.deliveryArea = None
        self.hopeArrivalTime = None
        self.invoiceFlag = None
        self.invoiceName = None
        self.invoiceType = None
        self.order = None
        self.orderId = None
        self.postFee = None
        self.receiverAddress = None
        self.receiverCity = None
        self.receiverDistrict = None
        self.receiverMobile = None
        self.receiverName = None
        self.receiverPhone = None
        self.receiverState = None
        self.receiverTown = None
        self.receiverZip = None
        self.sellerNick = None
        
        self.setParamRule({
        	'buyerNick':{'allow_empty':False},
        	'deliveryArea':{'allow_empty':False},
        	'invoiceFlag':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'receiverDistrict':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	'receiverState':{'allow_empty':False},
        	'receiverTown':{'allow_empty':False},
        	'sellerNick':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPushOrder'

    def getApiMethod(self):

        return 'suning.pptv.pushorder.add'



