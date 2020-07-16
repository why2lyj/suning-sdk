# -*- coding: utf-8 -*-

'''

Created on 2016-2-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class CategoryMasDataQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryName = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'categoryName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCategoryMasData'

    def getApiMethod(self):

        return 'suning.fourps.categorymasdata.query'



