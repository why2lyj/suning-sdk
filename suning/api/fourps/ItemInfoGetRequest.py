# -*- coding: utf-8 -*-

'''

Created on 2016-8-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemInfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCmCode = None
        self.productName = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getItemInfo'

    def getApiMethod(self):

        return 'suning.fourps.iteminfo.get'



