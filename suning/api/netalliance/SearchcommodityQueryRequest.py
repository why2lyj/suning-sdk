# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class SearchcommodityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.branch = None
        self.cityCode = None
        self.coupon = None
        self.couponMark = None
        self.endPrice = None
        self.keyword = None
        self.pageIndex = None
        self.pgSearch = None
        self.picHeight = None
        self.picWidth = None
        self.saleCategoryCode = None
        self.size = None
        self.snfwservice = None
        self.snhwg = None
        self.sortType = None
        self.startPrice = None
        self.suningService = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'querySearchcommodity'

    def getApiMethod(self):

        return 'suning.netalliance.searchcommodity.query'



