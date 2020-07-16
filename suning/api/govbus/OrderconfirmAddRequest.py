# -*- coding: utf-8 -*-

'''

Created on 2019-3-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderconfirmAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addOrderconfirm'

    def getApiMethod(self):

        return 'suning.govbus.orderconfirm.add'



