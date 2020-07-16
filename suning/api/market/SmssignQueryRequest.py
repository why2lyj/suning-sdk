# -*- coding: utf-8 -*-

'''

Created on 2019-11-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class SmssignQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySmssign'

    def getApiMethod(self):

        return 'suning.market.smssign.query'



