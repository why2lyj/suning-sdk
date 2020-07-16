# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class SelectrecommendcommodityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityCode = None
        self.couponMark = None
        self.eliteId = None
        self.pageIndex = None
        self.picHeight = None
        self.picWidth = None
        self.selfSupport = None
        self.size = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'querySelectrecommendcommodity'

    def getApiMethod(self):

        return 'suning.netalliance.selectrecommendcommodity.query'



