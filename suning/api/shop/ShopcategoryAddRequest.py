# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopcategoryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.shopCategory = None



    def getApiBizName(self):

        return 'addCategory'



    def getApiMethod(self):

        return 'suning.custom.shopcategory.add'



