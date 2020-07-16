# -*- coding: utf-8 -*-

'''

Created on 2019-3-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class ElectronicInvoiceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invoiceAmount = None
        self.invoiceCode = None
        self.invoiceData = None
        self.invoiceFlag = None
        self.invoiceHead = None
        self.invoiceHeadType = None
        self.invoiceNo = None
        self.invoiceNoTaxAmount = None
        self.invoiceSecurityCode = None
        self.invoiceTime = None
        self.invoiceType = None
        self.logisticsComp = None
        self.logisticsOrderId = None
        self.oldInvoiceCode = None
        self.oldInvoiceNum = None
        self.orderId = None
        self.productCode = None
        
        self.setParamRule({
        	'invoiceAmount':{'allow_empty':False},
        	'invoiceCode':{'allow_empty':False},
        	'invoiceData':{'allow_empty':False},
        	'invoiceFlag':{'allow_empty':False},
        	'invoiceHead':{'allow_empty':False},
        	'invoiceHeadType':{'allow_empty':False},
        	'invoiceNo':{'allow_empty':False},
        	'invoiceTime':{'allow_empty':False},
        	'invoiceType':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addElectronicInvoice'

    def getApiMethod(self):

        return 'suning.custom.electronicinvoice.add'



