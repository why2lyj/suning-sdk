# -*- coding: utf-8 -*-

'''

Created on 2020-2-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoorderUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.payDate = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'payDate':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateOtoorder'

    def getApiMethod(self):

        return 'suning.onlinestore.order.update'



