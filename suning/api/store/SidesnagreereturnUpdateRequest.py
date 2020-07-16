# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnagreereturnUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.returnQuestId = None
        self.sendType = None
        
        self.setParamRule({
        	'returnQuestId':{'allow_empty':False},
        	'sendType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateSidesnagreereturn'

    def getApiMethod(self):

        return 'suning.store.sidesnagreereturn.update'



