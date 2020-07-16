# -*- coding: utf-8 -*-

'''

Created on 2016-1-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDetailQueryRequest(AbstractApi):

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

        return 'queryOrderDetail'

    def getApiMethod(self):

        return 'suning.fourps.orderdetail.query'



