# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommoditypriceModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.productCode = None
        self.sellPrice = None
        self.storeCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'sellPrice':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyCommodityprice'

    def getApiMethod(self):

        return 'suning.store.commodityprice.modify'



