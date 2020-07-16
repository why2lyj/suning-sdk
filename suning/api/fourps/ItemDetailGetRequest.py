# -*- coding: utf-8 -*-

'''

Created on 2016-8-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCmCode = None
        self.productName = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getItemDetail'

    def getApiMethod(self):

        return 'suning.fourps.itemdetail.get'



