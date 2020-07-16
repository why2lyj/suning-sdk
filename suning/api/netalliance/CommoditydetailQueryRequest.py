# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommoditydetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityCode = None
        self.commodityStr = None
        self.couponMark = None
        self.picHeight = None
        self.picWidth = None
        
        self.setParamRule({
        	'commodityStr':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCommoditydetail'

    def getApiMethod(self):

        return 'suning.netalliance.commoditydetail.query'



