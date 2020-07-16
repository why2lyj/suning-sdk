# -*- coding: utf-8 -*-

'''

Created on 2018-9-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivitycoupondetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.shopCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'shopCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getActivitycoupondetail'

    def getApiMethod(self):

        return 'suning.custom.activitycoupondetail.get'



