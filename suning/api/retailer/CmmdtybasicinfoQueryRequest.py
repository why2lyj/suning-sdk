# -*- coding: utf-8 -*-

'''

Created on 2020-4-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtybasicinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cityCode = None
        self.cmmdtyList = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtybasicinfo'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtybasicinfo.query'



