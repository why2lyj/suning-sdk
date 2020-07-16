# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopcategoryDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None



    def getApiBizName(self):

        return 'deleteCategory'



    def getApiMethod(self):

        return 'suning.custom.shopcategory.delete'



