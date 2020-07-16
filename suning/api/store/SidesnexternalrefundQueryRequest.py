# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnexternalrefundQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderNo = None
        
        self.setParamRule({
        	'orderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySidesnexternalqueryrefund'

    def getApiMethod(self):

        return 'suning.store.sidesnexternalqueryrefund.query'



