# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuId = None
        
        self.setParamRule({
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getProdDetail'

    def getApiMethod(self):

        return 'suning.govbus.proddetail.get'



