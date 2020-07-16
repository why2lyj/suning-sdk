# -*- coding: utf-8 -*-

'''

Created on 2020-6-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class PxcardReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderLineNumber = None
        self.pxCardList = None
        
        self.setParamRule({
        	'orderLineNumber':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receivePxcard'

    def getApiMethod(self):

        return 'suning.custom.pxcard.receive'



