# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurchaseplanQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.purchasePlanNo = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'purchasePlanNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPurchaseplan'

    def getApiMethod(self):

        return 'suning.selfmarket.purchaseplan.query'



