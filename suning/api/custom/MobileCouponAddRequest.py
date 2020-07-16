# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MobileCouponAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.couponName = None
        self.couponInfo = None
        
        self.setParamRule({
        	'couponName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addMobileCoupon'

    def getApiMethod(self):

        return 'suning.custom.mobilecoupon.add'



