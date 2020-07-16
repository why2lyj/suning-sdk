# -*- coding: utf-8 -*-

'''

Created on 2018-1-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class LsypriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryLsyprice'

    def getApiMethod(self):

        return 'suning.custom.lsyprice.query'



