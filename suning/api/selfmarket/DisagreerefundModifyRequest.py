# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class DisagreerefundModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.fileName = None
        self.notReason = None
        self.omsOrderItemNo = None
        self.picProof = None
        self.supplierCode = None
        
        self.setParamRule({
        	'notReason':{'allow_empty':False},
        	'omsOrderItemNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyDisagreerefund'

    def getApiMethod(self):

        return 'suning.selfmarket.disagreerefund.modify'



