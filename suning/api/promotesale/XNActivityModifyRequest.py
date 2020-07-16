# -*- coding: utf-8 -*-

'''

Created on 2015-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class XNActivityModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.startTime = None
        self.endTime = None
        self.baseAmount = None
        self.rewardAmount = None
        self.isLimit = None
        self.peopleActivityTimesLimit = None
        self.peopleDayTimesLimit = None
        self.productList = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyXNActivity'

    def getApiMethod(self):

        return 'suning.custom.xnactivity.modify'



