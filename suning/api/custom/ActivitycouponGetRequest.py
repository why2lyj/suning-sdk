# -*- coding: utf-8 -*-

'''

Created on 2018-9-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivitycouponGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.memberId = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'memberId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getActivitycoupon'

    def getApiMethod(self):

        return 'suning.custom.activitycoupon.get'



