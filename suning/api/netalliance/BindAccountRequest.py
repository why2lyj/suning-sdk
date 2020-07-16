# -*- coding: utf-8 -*-

'''

Created on 2016-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class BindAccountRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.extSystemId = None
        self.extBusRef = None
        self.mixCustNum = None
        
        self.setParamRule({
        	'extSystemId':{'allow_empty':False},
        	'extBusRef':{'allow_empty':False},
        	'mixCustNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'bindAccount'

    def getApiMethod(self):

        return 'suning.netalliance.account.bind'



