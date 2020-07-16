# -*- coding: utf-8 -*-

'''

Created on 2020-6-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class PasspartproductinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.spuId = None
        self.supplierCode = None
        
        self.setParamRule({
        	'spuId':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPasspartproductinfo'

    def getApiMethod(self):

        return 'suning.sngoods.passpartproductinfo.query'



