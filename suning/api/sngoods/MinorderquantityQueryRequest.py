# -*- coding: utf-8 -*-

'''

Created on 2020-2-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class MinorderquantityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skus = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryMinorderquantity'

    def getApiMethod(self):

        return 'suning.sngoods.minorderquantity.query'



