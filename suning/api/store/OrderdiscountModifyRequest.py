# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderdiscountModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.activityName = None
        self.appStoreCode = None
        self.endTime = None
        self.productList = None
        self.startTime = None
        self.storeCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyOrderdiscount'

    def getApiMethod(self):

        return 'suning.store.orderdiscount.modify'



