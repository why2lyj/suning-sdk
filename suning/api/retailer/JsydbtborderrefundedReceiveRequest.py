# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydbtborderrefundedReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.refundStatus = None
        self.token = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'refundStatus':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveJsydbtborderrefunded'

    def getApiMethod(self):

        return 'suning.retailer.jsydbtborderrefunded.receive'



