# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionUnitGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionUnitId = None
        
        self.setParamRule({
        	'promotionUnitId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPromotionUnit'

    def getApiMethod(self):

        return 'suning.advertise.promotionunit.get'



