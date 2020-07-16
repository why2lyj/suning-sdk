# -*- coding: utf-8 -*-

'''

Created on 2018-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemcontentsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryItemcontents'

    def getApiMethod(self):

        return 'suning.saleoff.itemcontents.query'



