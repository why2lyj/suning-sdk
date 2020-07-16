# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class RetchggoodsCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.operateType = None
        self.orderId = None
        self.orderItems = None
        
        self.setParamRule({
        	'operateType':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'cancelRetchggoods'

    def getApiMethod(self):

        return 'suning.govbus.retchggoods.cancel'



