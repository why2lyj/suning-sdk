# -*- coding: utf-8 -*-

'''

Created on 2017-3-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExpressorderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.expressCompCode = None
        self.marketingProduct = None
        self.orderSource = None
        self.packageList = None
        self.receiverAddressDetail = None
        self.receiverCity = None
        self.receiverCompany = None
        self.receiverDistrict = None
        self.receiverMobile = None
        self.receiverName = None
        self.receiverProvince = None
        self.receiverTel = None
        self.receiverTown = None
        self.senderAddressDetail = None
        self.senderCity = None
        self.senderCompany = None
        self.senderDistrict = None
        self.senderMobile = None
        self.senderName = None
        self.senderProvince = None
        self.senderTel = None
        self.senderTown = None
        self.uuid = None
        
        self.setParamRule({
        	'expressCompCode':{'allow_empty':False},
        	'marketingProduct':{'allow_empty':False},
        	'orderSource':{'allow_empty':False},
        	'receiverAddressDetail':{'allow_empty':False},
        	'receiverCity':{'allow_empty':False},
        	'receiverDistrict':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	'receiverProvince':{'allow_empty':False},
        	'senderAddressDetail':{'allow_empty':False},
        	'senderCity':{'allow_empty':False},
        	'senderDistrict':{'allow_empty':False},
        	'senderName':{'allow_empty':False},
        	'senderProvince':{'allow_empty':False},
        	'uuid':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addExpressorder'

    def getApiMethod(self):

        return 'suning.fourps.expressorder.add'



