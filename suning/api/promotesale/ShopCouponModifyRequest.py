# -*- coding: utf-8 -*-

'''

Created on 2015-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopCouponModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.activityCode = None
        self.activityTimesLimit = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyShopCoupon'

    def getApiMethod(self):

        return 'suning.custom.shopcoupon.modify'



