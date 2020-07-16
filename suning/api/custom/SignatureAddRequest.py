# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class SignatureAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.businessLincenseFileContent = None
        self.businessLincenseFileSuffix = None
        self.certificateType = None
        self.name = None
        self.orgCodeFileContent = None
        self.orgCodeFileSuffix = None
        self.remark = None
        self.screenshotFileContent = None
        self.screenshotFileSuffix = None
        self.sourceName = None
        self.subject = None
        self.taxationFileContent = None
        self.taxationFileSuffix = None
        self.threeInOneFileContent = None
        self.threeInOneFileSuffix = None
        self.timeStamp = None
        self.userId = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'certificateType':{'allow_empty':False},
        	'name':{'allow_empty':False},
        	'remark':{'allow_empty':False},
        	'sourceName':{'allow_empty':False},
        	'subject':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addSignature'

    def getApiMethod(self):

        return 'suning.custom.signature.add'



