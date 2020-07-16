# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MobileRecommendModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.operation = None
        self.recommendId = None
        self.recommendName = None
        self.productInfo = None
        
        self.setParamRule({
        	'recommendId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyMobileRecommend'

    def getApiMethod(self):

        return 'suning.custom.mobilerecommend.modify'



