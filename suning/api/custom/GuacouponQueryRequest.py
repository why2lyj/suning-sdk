# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class GuacouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.activityStatus = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.shopCode = None
        self.startTime = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'shopCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryGuacoupon'

    def getApiMethod(self):

        return 'suning.custom.guacoupon.query'



