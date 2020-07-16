# -*- coding: utf-8 -*-

'''

Created on 2018-4-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class CategorysearchQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.searchContent = None
        
        self.setParamRule({
        	'searchContent':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCategorysearch'

    def getApiMethod(self):

        return 'suning.govbus.categorysearch.query'



