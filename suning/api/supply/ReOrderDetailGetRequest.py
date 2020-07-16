# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReOrderDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.b2cOrderNo = None
        
        self.setParamRule({
        	'b2cOrderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getReOrderDetail'

    def getApiMethod(self):

        return 'suning.supply.reorderdetail.get'



