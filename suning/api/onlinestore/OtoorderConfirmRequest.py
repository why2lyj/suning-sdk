# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoorderConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmOtoorder'

    def getApiMethod(self):

        return 'suning.onlinestore.order.confirm'



