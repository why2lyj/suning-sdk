# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopfavoriteAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channel = None
        self.custNum = None
        self.entrance = None
        self.shopId = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False},
        	'shopId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addShopaddfavorite'

    def getApiMethod(self):

        return 'suning.custom.shopaddfavorite.add'



