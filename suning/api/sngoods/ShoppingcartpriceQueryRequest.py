# -*- coding: utf-8 -*-

'''

Created on 2020-2-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShoppingcartpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelCode = None
        self.cityCode = None
        self.cmmdtyInfoList = None
        self.regionCode = None
        
        self.setParamRule({
        	'channelCode':{'allow_empty':False},
        	'cityCode':{'allow_empty':False},
        	'regionCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryShoppingcartprice'

    def getApiMethod(self):

        return 'suning.sngoods.shoppingcartprice.query'



