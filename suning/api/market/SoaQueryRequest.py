# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class SoaQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySoa'

    def getApiMethod(self):

        return 'suning.market.soa.query'



