# -*- coding: utf-8 -*-

'''

Created on 2018-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemDetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'itemDetail'

    def getApiMethod(self):

        return 'suning.custom.itemdetail.query'



