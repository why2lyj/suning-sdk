# -*- coding: utf-8 -*-

'''

Created on 2018-1-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class LsypriceModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.productCode = None
        self.sellingPrice = None
        
        self.setParamRule({
        	'sellingPrice':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyLsyprice'

    def getApiMethod(self):

        return 'suning.custom.lsyprice.modify'



