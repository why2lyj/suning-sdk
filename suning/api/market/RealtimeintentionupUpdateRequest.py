# -*- coding: utf-8 -*-

'''

Created on 2019-4-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class RealtimeintentionupUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateRealtimeintentionup'

    def getApiMethod(self):

        return 'suning.market.realtimeintentionup.update'



