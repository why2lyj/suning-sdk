# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SsshopcouponGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.appStoreCode = None
        self.shopCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getSsshopcoupon'

    def getApiMethod(self):

        return 'suning.store.ssshopcoupon.get'



