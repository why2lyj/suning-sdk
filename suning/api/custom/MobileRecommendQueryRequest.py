# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MobileRecommendQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryMobileRecommend'

    def getApiMethod(self):

        return 'suning.custom.mobilerecommend.query'



