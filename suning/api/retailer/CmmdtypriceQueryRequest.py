# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtypriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.cmmdtyList = None
        self.merchantCustNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtyprice'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtyprice.query'



