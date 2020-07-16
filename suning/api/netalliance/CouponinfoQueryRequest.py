# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class CouponinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.couponNum = None
        self.quanUrl = None
        
        self.setParamRule({
        	'quanUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCouponinfo'

    def getApiMethod(self):

        return 'suning.netalliance.couponinfo.query'



