# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BookitemGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmTitle = None
        self.itemCode = None
        self.productCode = None
        self.productName = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'item'

    def getApiMethod(self):

        return 'suning.custom.bookitem.get'



