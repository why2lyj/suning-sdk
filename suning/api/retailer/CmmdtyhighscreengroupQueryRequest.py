# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyhighscreengroupQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.keyword = None
        self.purchaseType = None
        self.showCategoryCode = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'purchaseType':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtyhighscreengroup'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtyhighscreengroup.query'



