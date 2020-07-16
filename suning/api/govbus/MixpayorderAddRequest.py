# -*- coding: utf-8 -*-

'''

Created on 2020-3-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class MixpayorderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.amount = None
        self.cityId = None
        self.companyCustNo = None
        self.countyId = None
        self.email = None
        self.hopeArrivalTime = None
        self.invoiceContent = None
        self.invoiceState = None
        self.invoiceTitle = None
        self.invoiceType = None
        self.mobile = None
        self.orderType = None
        self.payment = None
        self.provinceId = None
        self.receiverName = None
        self.remark = None
        self.servFee = None
        self.sku = None
        self.specialVatTicket = None
        self.subPaymentModes = None
        self.telephone = None
        self.townId = None
        self.tradeNo = None
        self.zip = None
        
        self.setParamRule({
        	'address':{'allow_empty':False},
        	'amount':{'allow_empty':False},
        	'cityId':{'allow_empty':False},
        	'countyId':{'allow_empty':False},
        	'invoiceState':{'allow_empty':False},
        	'mobile':{'allow_empty':False},
        	'orderType':{'allow_empty':False},
        	'payment':{'allow_empty':False},
        	'provinceId':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	'servFee':{'allow_empty':False},
        	'tradeNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addMixpayorder'

    def getApiMethod(self):

        return 'suning.govbus.mixpayorder.add'



