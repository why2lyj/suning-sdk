# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class MpStockQueryRequest(AbstractApi):

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

        return 'queryMpStock'

    def getApiMethod(self):

        return 'suning.govbus.mprodstock.query'



