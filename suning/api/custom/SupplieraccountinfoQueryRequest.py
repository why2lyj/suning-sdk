# -*- coding: utf-8 -*-

'''

Created on 2019-12-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SupplieraccountinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'querySupplieraccountinfo'

    def getApiMethod(self):

        return 'suning.custom.supplieraccountinfo.query'



