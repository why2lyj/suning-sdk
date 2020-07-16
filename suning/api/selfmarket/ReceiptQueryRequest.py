# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReceiptQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endReceivedDate = None
        self.orderCode = None
        self.receivedCode = None
        self.startReceivedDate = None
        self.vendorRefNo = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'receiptQuery'

    def getApiMethod(self):

        return 'suning.selfmarket.receipt.query'



