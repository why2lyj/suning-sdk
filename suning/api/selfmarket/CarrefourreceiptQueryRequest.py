# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class CarrefourreceiptQueryRequest(AbstractApi):

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
        	})

    def getApiBizName(self):

        return 'queryCarrefourreceipt'

    def getApiMethod(self):

        return 'suning.selfmarket.carrefourreceipt.query'



