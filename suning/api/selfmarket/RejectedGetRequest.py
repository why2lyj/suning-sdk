# -*- coding: utf-8 -*-

'''

Created on 2019-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectedGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyTime = None
        self.omsOrderItemNo = None
        self.supplierCode = None
        self.workOrderNum = None
        
        self.setParamRule({
        	'omsOrderItemNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getRejected'

    def getApiMethod(self):

        return 'suning.selfmarket.rejected.get'



