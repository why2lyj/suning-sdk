# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class MonthproduceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.monthProduce = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addMonthproduce'

    def getApiMethod(self):

        return 'suning.selfmarket.monthproduce.add'



