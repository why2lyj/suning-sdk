# -*- coding: utf-8 -*-

'''

Created on 2016-2-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class VerifycodeAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.childAccountName = None
        self.orderItemList = None
        
        self.setParamRule({
        	'childAccountName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getVerifyCode'

    def getApiMethod(self):

        return 'suning.custom.verifycode.get'



