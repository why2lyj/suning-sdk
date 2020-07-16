# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class SearchcartonecouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chanId = None
        self.city = None
        self.mainProductList = None
        self.memberNo = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'memberNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySearchcartonecoupon'

    def getApiMethod(self):

        return 'suning.online.searchcartonecoupon.query'



