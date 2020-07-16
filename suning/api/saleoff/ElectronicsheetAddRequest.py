# -*- coding: utf-8 -*-

'''

Created on 2018-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ElectronicsheetAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'orderItemNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addElectronicsheet'

    def getApiMethod(self):

        return 'suning.saleoff.electronicsheet.add'



