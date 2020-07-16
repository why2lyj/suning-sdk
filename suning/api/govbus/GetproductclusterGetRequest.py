# -*- coding: utf-8 -*-

'''

Created on 2017-7-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetproductclusterGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuId = None
        
        self.setParamRule({
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getGetproductcluster'

    def getApiMethod(self):

        return 'suning.govbus.getproductcluster.get'



