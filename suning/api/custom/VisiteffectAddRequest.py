# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class VisiteffectAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.memberId = None
        self.statisTime = None
        self.snUnionId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'statisTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addVisiteffect'

    def getApiMethod(self):

        return 'suning.custom.visiteffect.add'



