# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class MsgtaskCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appCode = None
        self.appSecret = None
        self.content = None
        self.interestActivityId = None
        self.interestType = None
        self.longUrl = None
        self.paramJson = None
        self.shortUrl = None
        self.sign = None
        self.taskChannel = None
        self.template = None
        
        self.setParamRule({
        	'content':{'allow_empty':False},
        	'interestType':{'allow_empty':False},
        	'sign':{'allow_empty':False},
        	'taskChannel':{'allow_empty':False},
        	'template':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createMsgtask'

    def getApiMethod(self):

        return 'suning.custom.msgtask.create'



