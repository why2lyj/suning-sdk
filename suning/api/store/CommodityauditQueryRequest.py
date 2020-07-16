# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommodityauditQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.auditStatus = None
        self.auditType = None
        self.pageNo = None
        self.pageSize = None
        self.storeCode = None
        
        self.setParamRule({
        	'auditStatus':{'allow_empty':False},
        	'auditType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCommodityaudit'

    def getApiMethod(self):

        return 'suning.store.commodityaudit.query'



