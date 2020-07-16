# -*- coding: utf-8 -*-

'''

Created on 2020-2-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdpoolQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.channelCode = None
        
        self.setParamRule({
        	'channelCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryProdpool'

    def getApiMethod(self):

        return 'suning.sngoods.prodpool.query'



