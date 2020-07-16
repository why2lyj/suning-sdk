# -*- coding: utf-8 -*-

'''

Created on 2020-2-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoselfcodeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.shopCode = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'shopCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOtoselfcode'

    def getApiMethod(self):

        return 'suning.onlinestore.selfcode.query'



