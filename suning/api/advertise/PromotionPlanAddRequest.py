# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionPlanAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionName = None
        self.promotionStartDate = None
        self.promotionEndDate = None
        self.userLimitAmount = None
        self.mobileTerminalDiscount = None
        
        self.setParamRule({
        	'promotionName':{'allow_empty':False},
        	'promotionStartDate':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addPromotionPlan'

    def getApiMethod(self):

        return 'suning.advertise.promotionplan.add'



