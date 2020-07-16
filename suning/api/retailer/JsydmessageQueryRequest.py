# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydmessageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.token = None
        self.type = None
        
        self.setParamRule({
        	'token':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryJsydmessage'

    def getApiMethod(self):

        return 'suning.retailer.jsydmessage.query'



