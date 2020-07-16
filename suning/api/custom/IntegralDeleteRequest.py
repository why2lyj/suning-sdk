# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class IntegralDeleteRequest(AbstractApi):

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

        return 'deleteIntegral'

    def getApiMethod(self):

        return 'suning.custom.integral.delete'



