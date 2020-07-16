# -*- coding: utf-8 -*-

'''

Created on 2019-8-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShelvesAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyCodes = None
        self.saleStatus = None
        self.storeCode = None
        
        self.setParamRule({
        	'saleStatus':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addShelves'

    def getApiMethod(self):

        return 'suning.restura.shelves.add'



