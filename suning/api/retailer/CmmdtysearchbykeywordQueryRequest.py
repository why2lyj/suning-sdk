# -*- coding: utf-8 -*-

'''

Created on 2020-3-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtysearchbykeywordQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.filters = None
        self.keyword = None
        self.pnumber = None
        self.psize = None
        self.purchaseType = None
        self.sort = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'keyword':{'allow_empty':False},
        	'pnumber':{'allow_empty':False},
        	'psize':{'allow_empty':False},
        	'purchaseType':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtysearchbykeyword'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtysearchbykeyword.query'



