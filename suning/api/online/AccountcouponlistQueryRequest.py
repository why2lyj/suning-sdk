# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class AccountcouponlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chanId = None
        self.couponStatus = None
        self.couponType = None
        self.memberId = None
        self.page = None
        self.perpageNumber = None
        self.timeRange = None
        self.timeType = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'couponStatus':{'allow_empty':False},
        	'couponType':{'allow_empty':False},
        	'memberId':{'allow_empty':False},
        	'page':{'allow_empty':False},
        	'perpageNumber':{'allow_empty':False},
        	'timeRange':{'allow_empty':False},
        	'timeType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryAccountcouponlist'

    def getApiMethod(self):

        return 'suning.online.accountcouponlist.query'



