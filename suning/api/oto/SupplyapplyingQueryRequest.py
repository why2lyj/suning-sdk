# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class SupplyapplyingQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.physicalCode = None
        self.applyStatus = None
        self.productName = None
        
        self.setParamRule({
        	'physicalCode':{'allow_empty':False},
        	'applyStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySupplyapplying'

    def getApiMethod(self):

        return 'suning.oto.supplyapplying.query'



