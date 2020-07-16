# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundAppointOrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.appointStatus = None
        self.refundType = None
        self.warehouseCode = None
        self.appointStartDate = None
        self.appointEndDate = None
        self.createStartDate = None
        self.createEndDate = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryRefundAppointOrder'

    def getApiMethod(self):

        return 'suning.swl.refundappointorder.query'



