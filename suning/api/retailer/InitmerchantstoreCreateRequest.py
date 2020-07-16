# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class InitmerchantstoreCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.coperator = None
        self.dyttInitMerchantInfoDTO = None
        self.dyttInitSotreInfoDTO = None
        self.operType = None
        self.platformCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createInitmerchantstore'

    def getApiMethod(self):

        return 'suning.retailer.initmerchantstore.create'



