# -*- coding: utf-8 -*-

'''

Created on 2014-7-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemsaleareaGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.itemCode = None



    def getApiBizName(self):

        return 'itemSalearea'



    def getApiMethod(self):

        return 'suning.custom.itemsalearea.get'



