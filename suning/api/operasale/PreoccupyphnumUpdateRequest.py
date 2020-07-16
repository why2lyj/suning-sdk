# -*- coding: utf-8 -*-

'''

Created on 2018-8-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class PreoccupyphnumUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.phoneNumber = None
        self.operType = None
        self.opId = None
        self.channelCode = None
        
        self.setParamRule({
        	'phoneNumber':{'allow_empty':False},
        	'operType':{'allow_empty':False},
        	'opId':{'allow_empty':False},
        	'channelCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updatePreoccupyphnum'

    def getApiMethod(self):

        return 'suning.operasale.preoccupyphnum.update'



