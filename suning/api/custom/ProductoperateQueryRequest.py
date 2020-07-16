# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductoperateQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.custNum = None
        self.cityId = None
        self.lesCityCode = None
        self.mdmCityCode = None
        self.pageSize = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False},
        	'cityId':{'allow_empty':False},
        	'lesCityCode':{'allow_empty':False},
        	'mdmCityCode':{'allow_empty':False},
        	'pageSize':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryProductoperate'

    def getApiMethod(self):

        return 'suning.custom.productoperate.query'



