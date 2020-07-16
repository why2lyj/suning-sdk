# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionUnitModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionUnitId = None
        self.goodsCode = None
        self.goodsUrl = None
        self.unitDetail = None
        
        self.setParamRule({
        	'promotionUnitId':{'allow_empty':False},
        	'goodsCode':{'allow_empty':False},
        	'goodsUrl':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyPromotionUnit'

    def getApiMethod(self):

        return 'suning.advertise.promotionunit.modify'



