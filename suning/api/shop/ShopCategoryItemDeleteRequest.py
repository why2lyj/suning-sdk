# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopCategoryItemDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.products = None



    def getApiBizName(self):

        return 'deleteCategoryItem'



    def getApiMethod(self):

        return 'suning.custom.shopcategoryitem.delete'



