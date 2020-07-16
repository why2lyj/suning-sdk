# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MobileCouponModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.operation = None
        self.couponId = None
        self.couponName = None
        self.couponInfo = None
        
        self.setParamRule({
        	'couponId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyMobileCoupon'

    def getApiMethod(self):

        return 'suning.custom.mobilecoupon.modify'



