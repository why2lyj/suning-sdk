# -*- coding: utf-8 -*-

'''

Created on 2020-2-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.amount = None
        self.channelcode = None
        self.cityId = None
        self.countyId = None
        self.hopeArrivalTime = None
        self.invoiceState = None
        self.invoiceTitle = None
        self.invoiceType = None
        self.mobile = None
        self.payment = None
        self.provinceId = None
        self.receiverName = None
        self.remark = None
        self.servFee = None
        self.sku = None
        self.specialVatTicket = None
        self.telephone = None
        self.townId = None
        self.tradeNo = None
        
        self.setParamRule({
        	'address':{'allow_empty':False},
        	'channelcode':{'allow_empty':False},
        	'cityId':{'allow_empty':False},
        	'countyId':{'allow_empty':False},
        	'invoiceState':{'allow_empty':False},
        	'mobile':{'allow_empty':False},
        	'payment':{'allow_empty':False},
        	'provinceId':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	'tradeNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addOrder'

    def getApiMethod(self):

        return 'suning.sngoods.order.add'



