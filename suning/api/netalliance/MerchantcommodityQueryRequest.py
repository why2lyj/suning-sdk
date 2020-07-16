# -*- coding: utf-8 -*-

'''

Created on 2017-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class MerchantcommodityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.pageNo = None
        self.pageSize = None
        self.adBookId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'adBookId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMerchantcommodity'

    def getApiMethod(self):

        return 'suning.netalliance.merchantcommodity.query'



