# -*- coding: utf-8 -*-

'''

Created on 2020-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.shopId = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryShopinfo'

    def getApiMethod(self):

        return 'suning.custom.shopinfo.query'



