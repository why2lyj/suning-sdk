# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class CaronegetcouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelId = None
        self.city = None
        self.memberId = None
        self.productList = None
        
        self.setParamRule({
        	'channelId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'memberId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCaronegetcoupon'

    def getApiMethod(self):

        return 'suning.online.caronegetcoupon.query'



