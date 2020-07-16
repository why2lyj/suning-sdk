# -*- coding: utf-8 -*-

'''

Created on 2018-10-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderitemdetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemIds = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getOrderitemdetail'

    def getApiMethod(self):

        return 'suning.govbus.orderitemdetail.get'



