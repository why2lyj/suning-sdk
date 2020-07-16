# -*- coding: utf-8 -*-

'''

Created on 2019-2-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReturnorderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getReturnorder'

    def getApiMethod(self):

        return 'suning.custom.returnorder.get'



