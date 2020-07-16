# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class QueryShopCouponRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.timeType = None
        self.startTime = None
        self.endTime = None
        self.couponStatusCode = None
        self.pageNo = None
        self.pageSize = None



    def getApiBizName(self):

        return 'queryShopCoupon'



    def getApiMethod(self):

        return 'suning.custom.shopcoupon.query'



