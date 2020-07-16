# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class TemplateAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.appCode = None
        self.code = None
        self.content = None
        self.description = None
        self.hideValue = None
        self.name = None
        self.smsDiffer = None
        self.smsType = None
        self.templateType = None
        self.timeStamp = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'content':{'allow_empty':False},
        	'description':{'allow_empty':False},
        	'name':{'allow_empty':False},
        	'smsType':{'allow_empty':False},
        	'templateType':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addTemplate'

    def getApiMethod(self):

        return 'suning.custom.template.add'



