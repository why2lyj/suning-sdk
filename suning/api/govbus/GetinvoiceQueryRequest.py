# -*- coding: utf-8 -*-

'''

Created on 2020-6-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetinvoiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.field = None
        self.type = None
        
        self.setParamRule({
        	'field':{'allow_empty':False},
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetinvoice'

    def getApiMethod(self):

        return 'suning.govbus.getinvoice.query'



