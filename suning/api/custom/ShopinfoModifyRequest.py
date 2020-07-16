# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopinfoModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.placard = None
        self.telphone = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'modifyShopinfo'

    def getApiMethod(self):

        return 'suning.custom.shopinfo.modify'



