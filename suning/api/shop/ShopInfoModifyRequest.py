# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopInfoModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.placard = None
        self.telphone = None



    def getApiBizName(self):

        return 'modifyShopInfo'



    def getApiMethod(self):

        return 'suning.custom.shopinfo.modify'



