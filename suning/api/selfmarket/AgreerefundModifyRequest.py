# -*- coding: utf-8 -*-

'''

Created on 2017-2-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreerefundModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.omsOrderItemNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'omsOrderItemNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyAgreerefund'

    def getApiMethod(self):

        return 'suning.selfmarket.agreerefund.modify'



