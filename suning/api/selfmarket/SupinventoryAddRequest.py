# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class SupinventoryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.inventory = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSupinventory'

    def getApiMethod(self):

        return 'suning.selfmarket.supinventory.add'



