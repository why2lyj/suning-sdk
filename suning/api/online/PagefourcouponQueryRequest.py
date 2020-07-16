# -*- coding: utf-8 -*-

'''

Created on 2020-1-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class PagefourcouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.businessSign = None
        self.chanId = None
        self.city = None
        self.cmmdtyCode = None
        self.marketingActivityType = None
        self.memberNo = None
        self.price = None
        self.saleNum = None
        
        self.setParamRule({
        	'businessSign':{'allow_empty':False},
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'marketingActivityType':{'allow_empty':False},
        	'memberNo':{'allow_empty':False},
        	'price':{'allow_empty':False},
        	'saleNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPagefourcoupon'

    def getApiMethod(self):

        return 'suning.online.pagefourcoupon.query'



