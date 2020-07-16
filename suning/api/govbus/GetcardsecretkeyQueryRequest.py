# -*- coding: utf-8 -*-

'''

Created on 2020-7-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetcardsecretkeyQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.currentPage = None
        self.gcOrderNo = None
        self.pageNumber = None
        
        self.setParamRule({
        	'currentPage':{'allow_empty':False},
        	'gcOrderNo':{'allow_empty':False},
        	'pageNumber':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetcardsecretkey'

    def getApiMethod(self):

        return 'suning.govbus.getcardsecretkey.query'



