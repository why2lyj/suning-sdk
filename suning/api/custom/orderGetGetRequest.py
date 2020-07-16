# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class orderGetGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'orderGet'

    def getApiMethod(self):

        return 'suning.custom.order.get'



