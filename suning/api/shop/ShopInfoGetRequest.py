# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopInfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)




    def getApiBizName(self):

        return 'getShopInfo'



    def getApiMethod(self):

        return 'suning.custom.shopinfo.get'



