# -*- coding: utf-8 -*-

'''

Created on 2018-9-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoreinventoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.merchantCustNo = None
        self.storeCode = None
        self.startTime = None
        self.endTime = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryStoreinventory'

    def getApiMethod(self):

        return 'suning.retailer.storeinventory.query'



