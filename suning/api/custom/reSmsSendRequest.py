# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class reSmsSendRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.countryCode = None
        self.externalMsgId = None
        self.gcsmsParams = None
        self.mobile = None
        self.needMatch = None
        self.signature = None
        self.smsAppCode = None
        self.smsAppSecret = None
        self.templateCode = None
        
        self.setParamRule({
        	'mobile':{'allow_empty':False},
        	'signature':{'allow_empty':False},
        	'smsAppCode':{'allow_empty':False},
        	'smsAppSecret':{'allow_empty':False},
        	'templateCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'resendSms'

    def getApiMethod(self):

        return 'suning.custom.sms.send'



