# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class InteractactivityeffectQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInteractactivityeffect'

    def getApiMethod(self):

        return 'suning.custom.interactactivityeffect.query'



