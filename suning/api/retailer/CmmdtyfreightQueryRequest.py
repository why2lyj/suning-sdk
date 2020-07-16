# -*- coding: utf-8 -*-

'''

Created on 2019-4-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyfreightQueryRequest(AbstractApi):

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

        return 'queryCmmdtyfreight'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtyfreight.query'



