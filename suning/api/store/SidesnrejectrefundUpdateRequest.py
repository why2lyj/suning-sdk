# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnrejectrefundUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.rejectImage = None
        self.rejectReason = None
        self.rejectReasonCode = None
        self.rejectReasonDesc = None
        self.returnQuestId = None
        
        self.setParamRule({
        	'rejectReason':{'allow_empty':False},
        	'returnQuestId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateSidesnrejectrefund'

    def getApiMethod(self):

        return 'suning.store.sidesnrejectrefund.update'



