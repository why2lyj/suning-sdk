# -*- coding: utf-8 -*-

'''

Created on 2020-6-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetmarkidinvoiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.currentPage = None
        self.markId = None
        self.pageNumber = None
        
        self.setParamRule({
        	'currentPage':{'allow_empty':False},
        	'markId':{'allow_empty':False},
        	'pageNumber':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetmarkidinvoice'

    def getApiMethod(self):

        return 'suning.govbus.getmarkidinvoice.query'



