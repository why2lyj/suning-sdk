# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.supplierBraComp = None
        self.supplierOffice = None
        self.snCode = None
        self.supplierApplicationCode = None
        self.productBrand = None
        self.expenseBudgetCode = None
        self.areaCopCode = None
        self.startDate = None
        self.endDate = None
        self.promotActivName = None
        self.promotAgreementName = None
        self.paymentLittleMount = None
        self.settlementType = None
        self.invoiceDate = None
        self.payType = None
        self.invoiceContent = None
        self.payDate = None
        self.htmlContent = None
        self.signNatureContent = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	'snCode':{'allow_empty':False},
        	'supplierApplicationCode':{'allow_empty':False},
        	'productBrand':{'allow_empty':False},
        	'areaCopCode':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'promotActivName':{'allow_empty':False},
        	'paymentLittleMount':{'allow_empty':False},
        	'settlementType':{'allow_empty':False},
        	'invoiceContent':{'allow_empty':False},
        	'payDate':{'allow_empty':False},
        	'htmlContent':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'applyPromotionApplication'

    def getApiMethod(self):

        return 'suning.application.promotion.apply'



