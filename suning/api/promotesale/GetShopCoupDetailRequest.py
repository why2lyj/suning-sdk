# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetShopCoupDetailRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.couponId = None



    def getApiBizName(self):

        return 'getShopCoupDetail'



    def getApiMethod(self):

        return 'suning.custom.shopcoupdetail.get'



