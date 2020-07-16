# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class TemplateGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.code = None
        self.timeStamp = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'code':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getTemplate'

    def getApiMethod(self):

        return 'suning.custom.template.get'



