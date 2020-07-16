# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class IntegralCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.endTime = None
        self.integralRwardInfos = None
        self.shopCode = None
        self.startTime = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'shopCode':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createIntegral'

    def getApiMethod(self):

        return 'suning.custom.integral.create'



