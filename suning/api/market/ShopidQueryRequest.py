# -*- coding: utf-8 -*-

'''

Created on 2019-12-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopidQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryShopid'

    def getApiMethod(self):

        return 'suning.market.shopid.query'



