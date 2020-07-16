# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.positionNames = None
        self.webSiteId = None
        
        self.setParamRule({
        	'positionNames':{'allow_empty':False},
        	'webSiteId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createPromotion'

    def getApiMethod(self):

        return 'suning.netalliance.promotion.create'



