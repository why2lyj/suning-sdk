# -*- coding: utf-8 -*-

'''

Created on 2020-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class InteractactivityGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getInteractactivity'

    def getApiMethod(self):

        return 'suning.custom.interactactivity.get'



