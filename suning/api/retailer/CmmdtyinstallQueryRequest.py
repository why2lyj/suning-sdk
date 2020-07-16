# -*- coding: utf-8 -*-

'''

Created on 2018-11-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyinstallQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyList = None
        self.merchantCustNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtyinstall'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtyinstall.query'



