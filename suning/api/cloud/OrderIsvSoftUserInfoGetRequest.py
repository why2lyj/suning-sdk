# -*- coding: utf-8 -*-

'''

Created on 2015-6-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderIsvSoftUserInfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderIsvSoftUserInfo'

    def getApiMethod(self):

        return 'suning.cloud.orderisvsoftuserinfo.get'



