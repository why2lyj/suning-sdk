# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.classifyCode = None
        self.storeCode = None
        self.appStoreCode = None
        self.secondClassifyCode = None
        self.saleStatus = None
        self.productCode = None
        
        self.setParamRule({
        	'classifyCode':{'allow_empty':False},
        	'saleStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryProductlist'

    def getApiMethod(self):

        return 'suning.store.productlist.query'



