# -*- coding: utf-8 -*-

'''

Created on 2015-11-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderSource = None
        self.cancelType = None
        self.outOrderId = None
        
        self.setParamRule({
        	'orderSource':{'allow_empty':False},
        	'cancelType':{'allow_empty':False},
        	'outOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteOrder'

    def getApiMethod(self):

        return 'suning.fourps.order.delete'



