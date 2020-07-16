# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class JudgefacproductGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.skuIds = None
        
        self.setParamRule({
        	'cityId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getJudgefacproduct'

    def getApiMethod(self):

        return 'suning.govbus.judgefacproduct.get'



