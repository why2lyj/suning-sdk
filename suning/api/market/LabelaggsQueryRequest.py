# -*- coding: utf-8 -*-

'''

Created on 2019-12-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class LabelaggsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLabelaggs'

    def getApiMethod(self):

        return 'suning.market.labelaggs.query'



