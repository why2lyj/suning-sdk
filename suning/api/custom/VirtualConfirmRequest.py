# -*- coding: utf-8 -*-

'''

Created on 2018-6-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class VirtualConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cardList = None
        self.dealResult = None
        self.failedCode = None
        self.failedReason = None
        self.goodsSnap = None
        self.orderCode = None
        self.orderItemCode = None
        self.successTime = None
        
        self.setParamRule({
        	'dealResult':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'orderItemCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'confirmVirtual'

    def getApiMethod(self):

        return 'suning.custom.virtual.confirm'



