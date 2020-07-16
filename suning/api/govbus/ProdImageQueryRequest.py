# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdImageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuIds = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryProdImage'

    def getApiMethod(self):

        return 'suning.govbus.prodimage.query'



