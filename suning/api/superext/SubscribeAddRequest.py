# -*- coding: utf-8 -*-

'''

Created on 2020-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class SubscribeAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelCode = None
        self.cmmdtyCode = None
        self.cmmdtyName = None
        self.extOrderId = None
        self.mobileNum = None
        self.orderTime = None
        
        self.setParamRule({
        	'cmmdtyCode':{'allow_empty':False},
        	'extOrderId':{'allow_empty':False},
        	'mobileNum':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addSubscribe'

    def getApiMethod(self):

        return 'suning.superext.subscribe.add'



