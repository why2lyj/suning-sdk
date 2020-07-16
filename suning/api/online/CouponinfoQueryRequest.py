# -*- coding: utf-8 -*-

'''

Created on 2019-1-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class CouponinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.couponList = None
        self.mobileNum = None
        
        self.setParamRule({
        	'mobileNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCouponinfo'

    def getApiMethod(self):

        return 'suning.online.couponinfo.query'



