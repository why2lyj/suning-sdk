# -*- coding: utf-8 -*-

'''

Created on 2020-5-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GalaxiecouponGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.activitySecretKey = None
        self.appVersion = None
        self.bonusTrigerId = None
        self.cityId = None
        self.detect = None
        self.dfpToken = None
        self.idfToken = None
        self.memberId = None
        self.miniSource = None
        self.requestIp = None
        self.serialNo = None
        self.snUnionId = None
        self.terminalId = None
        self.termiSys = None
        self.valiNo = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'activitySecretKey':{'allow_empty':False},
        	'bonusTrigerId':{'allow_empty':False},
        	'detect':{'allow_empty':False},
        	'dfpToken':{'allow_empty':False},
        	'requestIp':{'allow_empty':False},
        	'terminalId':{'allow_empty':False},
        	'termiSys':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getGalaxiecoupon'

    def getApiMethod(self):

        return 'suning.custom.galaxiecoupon.get'



