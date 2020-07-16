# -*- coding: utf-8 -*-

'''

Created on 2020-3-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetspecialgoodsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryId = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'categoryId':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetspecialgoods'

    def getApiMethod(self):

        return 'suning.govbus.getspecialgoods.query'



