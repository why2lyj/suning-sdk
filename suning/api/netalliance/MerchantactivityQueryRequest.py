# -*- coding: utf-8 -*-

'''

Created on 2016-11-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class MerchantactivityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryMerchantactivity'

    def getApiMethod(self):

        return 'suning.netalliance.merchantactivity.query'



