# -*- coding: utf-8 -*-

'''

Created on 2019-9-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class ThirdpartyproductQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.detailUrl = None
        self.statParam = None
        
        self.setParamRule({
        	'detailUrl':{'allow_empty':False},
        	'statParam':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryThirdpartyproduct'

    def getApiMethod(self):

        return 'suning.netalliance.thirdpartyproduct.query'



