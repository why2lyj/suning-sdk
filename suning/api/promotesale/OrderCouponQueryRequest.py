# -*- coding: utf-8 -*-

'''

Created on 2016-1-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderCouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.status = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryOrderCoupon'

    def getApiMethod(self):

        return 'suning.custom.ordercoupon.query'



