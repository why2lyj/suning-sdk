# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class InteractactivityCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelInteractactivity'

    def getApiMethod(self):

        return 'suning.custom.interactactivity.cancel'



