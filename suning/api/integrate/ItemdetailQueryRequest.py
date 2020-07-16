# -*- coding: utf-8 -*-

'''

Created on 2020-4-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryItemdetail'

    def getApiMethod(self):

        return 'suning.integrate.itemdetail.query'



