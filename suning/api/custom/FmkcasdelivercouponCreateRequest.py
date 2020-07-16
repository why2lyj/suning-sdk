# -*- coding: utf-8 -*-

'''

Created on 2020-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class FmkcasdelivercouponCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.appToken = None
        self.appType = None
        self.buddleId = None
        self.businessScene = None
        self.clientIp = None
        self.couponsAmount = None
        self.deliverSource = None
        self.egoToken = None
        self.idNo = None
        self.invoker = None
        self.memberId = None
        self.pcToken = None
        self.phoneNo = None
        self.realName = None
        self.requestId = None
        self.requestKey = None
        self.requestNo = None
        self.terminalType = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'businessScene':{'allow_empty':False},
        	'deliverSource':{'allow_empty':False},
        	'invoker':{'allow_empty':False},
        	'memberId':{'allow_empty':False},
        	'requestId':{'allow_empty':False},
        	'requestNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createFmkcasdelivercoupon'

    def getApiMethod(self):

        return 'suning.custom.fmkcasdelivercoupon.create'



