# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectexchangedeliverModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.exchangeNo = None
        self.expressCompanyName = None
        self.expressNo = None
        self.memo = None
        self.reasonAgreenCode = None
        self.supplierCode = None
        
        self.setParamRule({
        	'exchangeNo':{'allow_empty':False},
        	'memo':{'allow_empty':False},
        	'reasonAgreenCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyRejectexchangedeliver'

    def getApiMethod(self):

        return 'suning.selfmarket.rejectexchangedeliver.modify'



