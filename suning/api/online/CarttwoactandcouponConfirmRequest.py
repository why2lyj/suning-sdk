# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class CarttwoactandcouponConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cartTwoNo = None
        self.chanId = None
        self.city = None
        self.couponUsedList = None
        self.mainProductList = None
        self.memberNo = None
        
        self.setParamRule({
        	'cartTwoNo':{'allow_empty':False},
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'memberNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmCarttwoactandcoupon'

    def getApiMethod(self):

        return 'suning.online.carttwoactandcoupon.confirm'



