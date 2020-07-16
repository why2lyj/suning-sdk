# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProtocolAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.supplierBraComp = None
        self.supplierOffice = None
        self.snCode = None
        self.supplierApplicationCode = None
        self.expenseBudgetCode = None
        self.areaCopCode = None
        self.contractDate = None
        self.contractCode = None
        self.adProtocolCity = None
        self.adProtocolRode = None
        self.adProtocolMarket = None
        self.adProtocolBuilding = None
        self.adProtocolArea = None
        self.startDate = None
        self.endDate = None
        self.paymentLittleMount = None
        self.firstMonthAmount = None
        self.secondPayMonth = None
        self.nextMonthAmount = None
        self.lastPayMonth = None
        self.lastMonthAmount = None
        self.settlementType = None
        self.otherProtocol = None
        self.htmlContent = None
        self.signNatureContent = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	'snCode':{'allow_empty':False},
        	'supplierApplicationCode':{'allow_empty':False},
        	'areaCopCode':{'allow_empty':False},
        	'adProtocolCity':{'allow_empty':False},
        	'adProtocolRode':{'allow_empty':False},
        	'adProtocolMarket':{'allow_empty':False},
        	'adProtocolBuilding':{'allow_empty':False},
        	'adProtocolArea':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'paymentLittleMount':{'allow_empty':False},
        	'settlementType':{'allow_empty':False},
        	'htmlContent':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'applyProtocolApplication'

    def getApiMethod(self):

        return 'suning.application.protocol.apply'



