# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetShoppingCouponRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.id = None



    def getApiBizName(self):

        return 'getShoppingCoupon'



    def getApiMethod(self):

        return 'suning.custom.shoppingcoupon.get'



