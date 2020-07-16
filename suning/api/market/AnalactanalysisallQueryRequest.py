# -*- coding: utf-8 -*-

'''

Created on 2019-9-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class AnalactanalysisallQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryAnalactanalysisall'

    def getApiMethod(self):

        return 'suning.market.analactanalysisall.query'



