# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionPlanQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionStartDate = None
        self.promotionEndDate = None
        
        self.setParamRule({
        	'promotionStartDate':{'allow_empty':False},
        	'promotionEndDate':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPromotionPlan'

    def getApiMethod(self):

        return 'suning.advertise.promotionplan.query'



