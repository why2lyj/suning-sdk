# -*- coding: utf-8 -*-

'''

Created on 2019-7-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class AnalactanalysisexportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryAnalactanalysisexport'

    def getApiMethod(self):

        return 'suning.market.analactanalysisexport.query'



