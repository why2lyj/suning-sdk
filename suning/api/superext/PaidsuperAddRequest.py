# -*- coding: utf-8 -*-

'''

Created on 2019-4-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class PaidsuperAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.amount = None
        self.appCode = None
        self.externalOrderNo = None
        self.externalUid = None
        self.extSystemId = None
        self.mixCustNum = None
        self.mobileNum = None
        self.payTime = None
        self.payType = None
        self.settlementAmount = None
        
        self.setParamRule({
        	'amount':{'allow_empty':False},
        	'appCode':{'allow_empty':False},
        	'externalOrderNo':{'allow_empty':False},
        	'externalUid':{'allow_empty':False},
        	'extSystemId':{'allow_empty':False},
        	'mobileNum':{'allow_empty':False},
        	'payTime':{'allow_empty':False},
        	'payType':{'allow_empty':False},
        	'settlementAmount':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPaidsuper'

    def getApiMethod(self):

        return 'suning.superext.paidsuper.add'



