# -*- coding: utf-8 -*-

'''

Created on 2018-3-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyCode = None
        self.productCode = None
        self.supplierCodeAsk = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryItemdetail'

    def getApiMethod(self):

        return 'suning.selfmarket.itemdetail.query'



