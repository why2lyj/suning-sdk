# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionUnitQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionId = None
        
        self.setParamRule({
        	'promotionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPromotionUnit'

    def getApiMethod(self):

        return 'suning.advertise.promotionunit.query'



