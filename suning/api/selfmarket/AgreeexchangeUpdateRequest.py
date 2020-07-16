# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreeexchangeUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.backinDate = None
        self.exchangeNo = None
        self.getBackPerson = None
        self.getBackPersonTel = None
        self.memo = None
        self.returnBackType = None
        self.supplierCode = None
        self.wareHouseCode = None
        
        self.setParamRule({
        	'exchangeNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateAgreeexchange'

    def getApiMethod(self):

        return 'suning.selfmarket.agreeexchange.update'



