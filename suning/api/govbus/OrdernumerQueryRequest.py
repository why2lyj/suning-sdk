# -*- coding: utf-8 -*-

'''

Created on 2017-12-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdernumerQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderIds = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryOrdernumer'

    def getApiMethod(self):

        return 'suning.govbus.ordernumber.query'



