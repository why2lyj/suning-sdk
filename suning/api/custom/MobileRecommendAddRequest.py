# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MobileRecommendAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.recommendName = None
        self.productInfo = None
        
        self.setParamRule({
        	'recommendName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addMobileRecommend'

    def getApiMethod(self):

        return 'suning.custom.mobilerecommend.add'



