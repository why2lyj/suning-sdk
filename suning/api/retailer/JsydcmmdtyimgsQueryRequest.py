# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydcmmdtyimgsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.sku = None
        self.token = None
        
        self.setParamRule({
        	'sku':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryJsydcmmdtyimgs'

    def getApiMethod(self):

        return 'suning.retailer.jsydcmmdtyimgs.query'



