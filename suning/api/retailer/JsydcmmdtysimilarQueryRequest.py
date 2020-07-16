# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydcmmdtysimilarQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuId = None
        self.token = None
        
        self.setParamRule({
        	'skuId':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryJsydcmmdtysimilar'

    def getApiMethod(self):

        return 'suning.retailer.jsydcmmdtysimilar.query'



