# -*- coding: utf-8 -*-

'''

Created on 2019-3-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdercancelDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'deleteOrdercancel'

    def getApiMethod(self):

        return 'suning.govbus.ordercancel.delete'



