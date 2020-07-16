# -*- coding: utf-8 -*-

'''

Created on 2018-9-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopfavoritedGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        self.shopId = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False},
        	'shopId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getShopfavorited'

    def getApiMethod(self):

        return 'suning.custom.shopfavorited.get'



