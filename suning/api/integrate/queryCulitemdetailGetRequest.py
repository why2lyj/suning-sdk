# -*- coding: utf-8 -*-

'''

Created on 2020-4-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class queryCulitemdetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryCulitemdetail'

    def getApiMethod(self):

        return 'suning.integrate.culitemdetail.get'



