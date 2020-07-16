# -*- coding: utf-8 -*-

'''

Created on 2015-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPromotion'

    def getApiMethod(self):

        return 'suning.custom.promotion.query'



