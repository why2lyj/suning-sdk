# -*- coding: utf-8 -*-

'''

Created on 2019-4-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnsubscribeDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appCode = None
        self.extSystemId = None
        self.mobileNum = None
        self.orderId = None
        self.payType = None
        self.unsubscribeTime = None
        
        self.setParamRule({
        	'appCode':{'allow_empty':False},
        	'extSystemId':{'allow_empty':False},
        	'mobileNum':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'deleteUnsubscribe'

    def getApiMethod(self):

        return 'suning.superext.unsubscribe.delete'



