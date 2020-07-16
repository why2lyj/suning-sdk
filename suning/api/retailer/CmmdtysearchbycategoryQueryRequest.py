# -*- coding: utf-8 -*-

'''

Created on 2020-3-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtysearchbycategoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.filters = None
        self.pnumber = None
        self.psize = None
        self.purchaseType = None
        self.showCategoryCode = None
        self.sort = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'pnumber':{'allow_empty':False},
        	'psize':{'allow_empty':False},
        	'purchaseType':{'allow_empty':False},
        	'showCategoryCode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtysearchbycategory'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtysearchbycategory.query'



