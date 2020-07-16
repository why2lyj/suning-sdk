# -*- coding: utf-8 -*-

'''

Created on 2020-2-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdersubmiCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.platFormTrade = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'createOrdersubmi'

    def getApiMethod(self):

        return 'suning.onlinestore.ordersubmit.create'



