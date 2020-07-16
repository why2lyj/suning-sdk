# -*- coding: utf-8 -*-

'''

Created on 2017-11-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class receiptQueryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endReceivedDate = None
        self.orderCode = None
        self.pageNo = None
        self.pageSize = None
        self.receivedCode = None
        self.startReceivedDate = None
        self.supplierCode = None
        self.vendorRefNo = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiptQuery'

    def getApiMethod(self):

        return 'suning.selfmarket.receiptsupplier.query'



