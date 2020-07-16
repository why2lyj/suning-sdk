# -*- coding: utf-8 -*-

'''

Created on 2018-4-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductsearchQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.aggregate = None
        self.attrList = None
        self.brandId = None
        self.categoryIdOne = None
        self.categoryIdThree = None
        self.categoryIdTwo = None
        self.cityCode = None
        self.limit = None
        self.max = None
        self.min = None
        self.page = None
        self.searchContent = None
        self.sortType = None
        
        self.setParamRule({
        	'cityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryProductsearch'

    def getApiMethod(self):

        return 'suning.govbus.productsearch.query'



