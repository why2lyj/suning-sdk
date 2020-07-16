# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityexecCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.giveAmount = None
        self.mixCustNum = None
        self.rewardLevel = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'mixCustNum':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createActivityexec'

    def getApiMethod(self):

        return 'suning.custom.activityexec.create'



