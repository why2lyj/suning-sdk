# -*- coding: utf-8 -*-

'''

Created on 2020-3-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class IndividualeinvoiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.gcItemNo = None
        self.gcOrderNo = None
        
        self.setParamRule({
        	'gcItemNo':{'allow_empty':False},
        	'gcOrderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryIndividualeinvoice'

    def getApiMethod(self):

        return 'suning.govbus.individualeinvoice.query'



