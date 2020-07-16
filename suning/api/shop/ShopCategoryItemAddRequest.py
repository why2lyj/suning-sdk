# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopCategoryItemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.products = None



    def getApiBizName(self):

        return 'addCategoryItem'



    def getApiMethod(self):

        return 'suning.custom.shopcategoryitem.add'



