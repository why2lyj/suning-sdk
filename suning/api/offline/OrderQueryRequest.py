# -*- coding: utf-8 -*-

'''

Created on 2019-1-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memNo = None
        self.rtStoreCode = None
        
        self.setParamRule({
        	'memNo':{'allow_empty':False},
        	'rtStoreCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrder'

    def getApiMethod(self):

        return 'suning.offline.order.query'



