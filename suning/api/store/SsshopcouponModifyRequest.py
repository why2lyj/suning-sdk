# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SsshopcouponModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.activityEndTime = None
        self.activityName = None
        self.activityStartTime = None
        self.appStoreCode = None
        self.circulation = None
        self.shopCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifySsshopcoupon'

    def getApiMethod(self):

        return 'suning.store.ssshopcoupon.modify'



