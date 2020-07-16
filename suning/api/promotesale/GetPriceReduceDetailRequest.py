# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetPriceReduceDetailRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.priceReduceId = None



    def getApiBizName(self):

        return 'getPriceReduce'



    def getApiMethod(self):

        return 'suning.custom.pricereducedetail.get'



