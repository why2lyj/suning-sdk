# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydbtborderCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.token = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelJsydbtborder'

    def getApiMethod(self):

        return 'suning.retailer.jsydbtborder.cancel'



