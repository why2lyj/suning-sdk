# -*- coding: utf-8 -*-

'''

Created on 2020-3-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtolistpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.businessType = None
        self.cityName = None
        self.cmmdtyInfo = None
        self.mapType = None
        self.outPoiId = None
        self.shopCode = None
        
        self.setParamRule({
        	'businessType':{'allow_empty':False},
        	'cityName':{'allow_empty':False},
        	'mapType':{'allow_empty':False},
        	'outPoiId':{'allow_empty':False},
        	'shopCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOtolistprice'

    def getApiMethod(self):

        return 'suning.onlinestore.listprice.query'



