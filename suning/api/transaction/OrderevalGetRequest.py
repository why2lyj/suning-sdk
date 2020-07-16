# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderevalGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        self.productCode = None



    def getApiBizName(self):

        return 'getOrderEval'



    def getApiMethod(self):

        return 'suning.custom.ordereval.get'



