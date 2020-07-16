# -*- coding: utf-8 -*-

'''

Created on 2016-2-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreeRefundModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.childAccountName = None
        self.code = None
        self.orderItemId = None
        self.returnMoney = None
        self.applyTime = None
        self.returnType = None
        
        self.setParamRule({
        	'childAccountName':{'allow_empty':False},
        	'code':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'returnMoney':{'allow_empty':False},
        	'applyTime':{'allow_empty':False},
        	'returnType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyAgreeRefund'

    def getApiMethod(self):

        return 'suning.custom.agreerefund.modify'



