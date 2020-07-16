# -*- coding: utf-8 -*-

'''

Created on 2020-5-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtypurchaseinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.appId = None
        self.cityCode = None
        self.cmmdtyList = None
        self.districtCode = None
        self.priceDate = None
        self.storeCode = None
        self.townCode = None
        
        self.setParamRule({
        	'address':{'allow_empty':False},
        	'appId':{'allow_empty':False},
        	'cityCode':{'allow_empty':False},
        	'districtCode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtypurchaseinfo'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtypurchaseinfo.query'



