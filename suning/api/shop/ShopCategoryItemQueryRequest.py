# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopCategoryItemQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.pageNo = None
        self.pageSize = None



    def getApiBizName(self):

        return 'queryCategoryItem'



    def getApiMethod(self):

        return 'suning.custom.shopcategoryitem.query'



