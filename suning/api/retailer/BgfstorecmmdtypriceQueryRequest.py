# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class BgfstorecmmdtypriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyList = None
        self.snStoreCode = None
        
        self.setParamRule({
        	'snStoreCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryBgfstorecmmdtyprice'

    def getApiMethod(self):

        return 'suning.retailer.bgfstorecmmdtyprice.query'



