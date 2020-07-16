# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class GuacouponModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.operationType = None
        self.shopCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'operationType':{'allow_empty':False},
        	'shopCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyGuacoupon'

    def getApiMethod(self):

        return 'suning.custom.guacoupon.modify'



