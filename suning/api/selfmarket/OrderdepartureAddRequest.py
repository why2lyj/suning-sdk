# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderdepartureAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderDepartue = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addOrderdeparture'

    def getApiMethod(self):

        return 'suning.selfmarket.orderdeparture.add'



