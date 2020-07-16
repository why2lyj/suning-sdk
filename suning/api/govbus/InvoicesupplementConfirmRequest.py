# -*- coding: utf-8 -*-

'''

Created on 2020-2-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoicesupplementConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyForInvoiceReqDTO = None
        self.orderInfoDTO = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmInvoicesupplement'

    def getApiMethod(self):

        return 'suning.govbus.invoicesupplement.confirm'



