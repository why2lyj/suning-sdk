# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SsshopcouponCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.appStoreCode = None
        self.operationType = None
        self.shopCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'operationType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'cancelSsshopcoupon'

    def getApiMethod(self):

        return 'suning.store.ssshopcoupon.cancel'



