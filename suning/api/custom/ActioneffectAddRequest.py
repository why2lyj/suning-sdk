# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActioneffectAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.memberId = None
        self.profitValue = None
        self.actionType = None
        self.statisTime = None
        self.snUnionId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'actionType':{'allow_empty':False},
        	'statisTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addActioneffect'

    def getApiMethod(self):

        return 'suning.custom.actioneffect.add'



