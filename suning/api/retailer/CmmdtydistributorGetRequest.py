# -*- coding: utf-8 -*-

'''

Created on 2018-11-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtydistributorGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyCode = None
        self.storeCode = None
        self.merchantCustNo = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCmmdtydistributor'

    def getApiMethod(self):

        return 'suning.retailer.distributorcode.get'



