# -*- coding: utf-8 -*-

'''

Created on 2019-8-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class SupplierplanAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.dataList = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSupplierplan'

    def getApiMethod(self):

        return 'suning.selfmarket.supplierplan.add'



