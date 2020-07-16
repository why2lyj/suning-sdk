# -*- coding: utf-8 -*-

'''

Created on 2020-5-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class SensitivewordsConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.content = None
        self.timeStamp = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'content':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmSensitivewords'

    def getApiMethod(self):

        return 'suning.custom.sensitivewords.confirm'



