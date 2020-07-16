# -*- coding: utf-8 -*-

'''

Created on 2016-2-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderCouponDetaiGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderCouponDetail'

    def getApiMethod(self):

        return 'suning.custom.ordercoupondetail.get'



