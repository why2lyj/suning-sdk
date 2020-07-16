# -*- coding: utf-8 -*-

'''

Created on 2020-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtodetailpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.businessType = None
        self.cityName = None
        self.cmmdtyCode = None
        self.mapType = None
        self.outPoiId = None
        self.saleNum = None
        self.shopCode = None
        
        self.setParamRule({
        	'businessType':{'allow_empty':False},
        	'cityName':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'mapType':{'allow_empty':False},
        	'outPoiId':{'allow_empty':False},
        	'saleNum':{'allow_empty':False},
        	'shopCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOtodetailprice'

    def getApiMethod(self):

        return 'suning.onlinestore.detailprice.query'



