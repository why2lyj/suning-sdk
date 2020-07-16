# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreereturnConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invAddrId = None
        self.remark = None
        self.returnApplyId = None
        
        self.setParamRule({
        	'invAddrId':{'allow_empty':False},
        	'remark':{'allow_empty':False},
        	'returnApplyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmAgreereturn'

    def getApiMethod(self):

        return 'suning.custom.agreereturn.confirm'



