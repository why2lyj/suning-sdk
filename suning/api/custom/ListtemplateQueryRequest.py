# -*- coding: utf-8 -*-

'''

Created on 2020-5-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class ListtemplateQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.appCode = None
        self.approved = None
        self.code = None
        self.createTimeEnd = None
        self.createTimeStart = None
        self.name = None
        self.pageNo = None
        self.pageSize = None
        self.smsDiffer = None
        self.smsType = None
        self.status = None
        self.templateType = None
        self.timeStamp = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryListtemplate'

    def getApiMethod(self):

        return 'suning.custom.template.query'



