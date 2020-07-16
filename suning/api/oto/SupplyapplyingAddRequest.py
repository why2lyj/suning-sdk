# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class SupplyapplyingAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.physicalCode = None
        self.price = None
        self.invQtyTar = None
        self.salesStatus = None
        self.childItem = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'physicalCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addSupplyapplying'

    def getApiMethod(self):

        return 'suning.oto.supplyapplying.add'



