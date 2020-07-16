# -*- coding: utf-8 -*-

'''

Created on 2019-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActtestsendcountQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryActtestsendcount'

    def getApiMethod(self):

        return 'suning.market.acttestsendcount.query'



