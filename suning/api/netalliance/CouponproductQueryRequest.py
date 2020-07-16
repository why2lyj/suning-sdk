# -*- coding: utf-8 -*-

'''

Created on 2017-10-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class CouponproductQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.positionId = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'positionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCouponproduct'

    def getApiMethod(self):

        return 'suning.netalliance.couponproduct.query'



