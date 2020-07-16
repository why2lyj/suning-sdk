# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreerefundConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.returnApplyId = None
        
        self.setParamRule({
        	'returnApplyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmAgreerefund'

    def getApiMethod(self):

        return 'suning.custom.agreerefund.confirm'



