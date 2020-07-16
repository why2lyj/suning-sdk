# -*- coding: utf-8 -*-

'''

Created on 2020-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class SyncrefundorderUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.batchRefundInfoList = None
        self.orderId = None
        self.refundFinishTime = None
        self.returnQuestId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'refundFinishTime':{'allow_empty':False},
        	'returnQuestId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateSyncrefundorder'

    def getApiMethod(self):

        return 'suning.onlinestore.syncrefundorder.update'



