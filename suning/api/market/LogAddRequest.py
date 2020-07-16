# -*- coding: utf-8 -*-

'''

Created on 2019-6-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addLog'

    def getApiMethod(self):

        return 'suning.market.log.add'



