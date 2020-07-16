# -*- coding: utf-8 -*-

'''

Created on 2016-1-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderCouponModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.activityProductList = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyOrderCoupon'

    def getApiMethod(self):

        return 'suning.custom.ordercoupon.modify'



