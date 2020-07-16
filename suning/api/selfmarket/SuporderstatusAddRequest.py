# -*- coding: utf-8 -*-

'''

Created on 2020-7-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class SuporderstatusAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supOrderStatus = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSuporderstatus'

    def getApiMethod(self):

        return 'suning.selfmarket.suporderstatus.add'



