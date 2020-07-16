# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangemessagesQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.changeApplyId = None
        
        self.setParamRule({
        	'changeApplyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryExchangemessages'

    def getApiMethod(self):

        return 'suning.custom.exchangemessages.query'



