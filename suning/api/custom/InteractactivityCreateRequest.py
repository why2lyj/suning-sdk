# -*- coding: utf-8 -*-

'''

Created on 2020-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class InteractactivityCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityDes = None
        self.activityName = None
        self.activityType = None
        self.endTime = None
        self.startTime = None
        self.storeCodes = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'activityType':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createInteractactivity'

    def getApiMethod(self):

        return 'suning.custom.interactactivity.create'



