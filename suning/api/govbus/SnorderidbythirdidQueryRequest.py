# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class SnorderidbythirdidQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.tradeNo = None
        
        self.setParamRule({
        	'tradeNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySnorderidbythirdid'

    def getApiMethod(self):

        return 'suning.govbus.snorderidbythirdid.query'



