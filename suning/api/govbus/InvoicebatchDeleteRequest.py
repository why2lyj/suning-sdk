# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoicebatchDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.batchInfos = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'deleteInvoicebatch'

    def getApiMethod(self):

        return 'suning.govbus.invoicebatch.delete'



