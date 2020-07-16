# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoinfoModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.autoRefund = None
        self.bookingShop = None
        self.childItem = None
        self.deductiblePrice = None
        self.effectiveDay = None
        self.extractMode = None
        self.insaleRefund = None
        self.payTemplate = None
        self.price = None
        self.priceType = None
        self.productCode = None
        self.saleDate = None
        self.saleSet = None
        self.sellChannel = None
        self.writeoffPayment = None
        self.writeoffShop = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyOtoinfo'

    def getApiMethod(self):

        return 'suning.custom.otoinfo.modify'



