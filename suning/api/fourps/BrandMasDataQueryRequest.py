# -*- coding: utf-8 -*-

'''

Created on 2016-2-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class BrandMasDataQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.brandName = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'brandName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryBrandMasData'

    def getApiMethod(self):

        return 'suning.fourps.brandmasdata.query'



