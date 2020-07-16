# -*- coding: utf-8 -*-

'''

Created on 2020-3-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtocartpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.businessType = None
        self.cityName = None
        self.cmmdtyInfo = None
        self.deliveryMode = None
        self.mapType = None
        self.outPoiId = None
        self.shopCode = None
        
        self.setParamRule({
        	'businessType':{'allow_empty':False},
        	'cityName':{'allow_empty':False},
        	'deliveryMode':{'allow_empty':False},
        	'mapType':{'allow_empty':False},
        	'outPoiId':{'allow_empty':False},
        	'shopCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOtocartprice'

    def getApiMethod(self):

        return 'suning.onlinestore.cartprice.query'



