# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.externalMsgId = None
        self.smsAppCode = None
        self.timeStamp = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'externalMsgId':{'allow_empty':False},
        	'smsAppCode':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryReport'

    def getApiMethod(self):

        return 'suning.custom.report.query'



