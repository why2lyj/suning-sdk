# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityallreleaseCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.allRelease = None
        self.remarks = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'allRelease':{'allow_empty':False},
        	'remarks':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelActivityallrelease'

    def getApiMethod(self):

        return 'suning.custom.activityallrelease.cancel'



