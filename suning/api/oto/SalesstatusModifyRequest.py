# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class SalesstatusModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.physicalCode = None
        self.salesStatus = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'physicalCode':{'allow_empty':False},
        	'salesStatus':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifySalesstatus'

    def getApiMethod(self):

        return 'suning.oto.salesstatus.modify'



