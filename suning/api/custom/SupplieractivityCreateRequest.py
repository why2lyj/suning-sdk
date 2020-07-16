# -*- coding: utf-8 -*-

'''

Created on 2019-12-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SupplieractivityCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.giveAmount = None
        self.giveMaxAmount = None
        self.isNeedPhone = None
        self.levelLimit = None
        self.remarks = None
        self.startTime = None
        self.thresholdAmount = None
        self.timesLimit = None
        self.totalAmount = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'giveMaxAmount':{'allow_empty':False},
        	'isNeedPhone':{'allow_empty':False},
        	'levelLimit':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'thresholdAmount':{'allow_empty':False},
        	'timesLimit':{'allow_empty':False},
        	'totalAmount':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createSupplieractivity'

    def getApiMethod(self):

        return 'suning.custom.supplieractivity.create'



