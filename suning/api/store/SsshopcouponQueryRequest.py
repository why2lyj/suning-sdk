# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SsshopcouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.activityShowStatus = None
        self.appStoreCode = None
        self.pageNo = None
        self.pageSize = None
        self.shopCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'querySsshopcoupon'

    def getApiMethod(self):

        return 'suning.store.ssshopcoupon.query'



