# -*- coding: utf-8 -*-

'''

Created on 2015-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class XNActivityAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.startTime = None
        self.endTime = None
        self.channelInfo = None
        self.baseAmount = None
        self.rewardAmount = None
        self.isLimit = None
        self.peopleActivityTimesLimit = None
        self.peopleDayTimesLimit = None
        self.productList = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'channelInfo':{'allow_empty':False},
        	'baseAmount':{'allow_empty':False},
        	'rewardAmount':{'allow_empty':False},
        	'isLimit':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addXNActivity'

    def getApiMethod(self):

        return 'suning.custom.xnactivity.add'



