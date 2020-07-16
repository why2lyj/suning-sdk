# -*- coding: utf-8 -*-

'''

Created on 2016-12-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.b2cOrderId = None
        
        self.setParamRule({
        	'b2cOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrder'

    def getApiMethod(self):

        return 'suning.oto.order.get'



