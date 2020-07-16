# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class QueryShoppingCouponRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.timeType = None
        self.startTime = None
        self.endTime = None
        self.statusCode = None
        self.range = None



    def getApiBizName(self):

        return 'queryShoppingCoupon'



    def getApiMethod(self):

        return 'suning.custom.shoppingcoupon.query'



