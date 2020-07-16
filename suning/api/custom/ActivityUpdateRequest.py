# -*- coding: utf-8 -*-

'''

Created on 2020-4-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityDes = None
        self.activityId = None
        self.activityName = None
        self.expectFlag = None
        self.expectTime = None
        self.strategyInstId = None
        self.taskId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'activityName':{'allow_empty':False},
        	'expectFlag':{'allow_empty':False},
        	'strategyInstId':{'allow_empty':False},
        	'taskId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateActivity'

    def getApiMethod(self):

        return 'suning.custom.activity.update'



