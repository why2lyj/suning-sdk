# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.counterCode = None
        self.itemInfo = None
        self.operateFlag = None
        self.payId = None
        
        self.setParamRule({
        	'operateFlag':{'allow_empty':False},
        	'payId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateOrder'

    def getApiMethod(self):

        return 'suning.offline.order.update'



