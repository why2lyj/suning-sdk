# -*- coding: utf-8 -*-

'''

Created on 2019-8-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommoditycategoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commoditycategoryList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryCommoditycategory'

    def getApiMethod(self):

        return 'suning.netalliance.commoditycategory.query'



