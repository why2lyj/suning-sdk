# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class MorerecommendGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityCode = None
        self.commodityCode = None
        self.picHeight = None
        self.picLocation = None
        self.picType = None
        self.picWidth = None
        self.supplierCode = None
        
        self.setParamRule({
        	'commodityCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getMorerecommend'

    def getApiMethod(self):

        return 'suning.netalliance.morerecommend.get'



