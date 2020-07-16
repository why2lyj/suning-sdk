# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnrefundreasonlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.queryType = None
        self.reasonType = None
        
        self.setParamRule({
        	'queryType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySidesnrefundreasonlist'

    def getApiMethod(self):

        return 'suning.store.sidesnrefundreasonlist.query'



