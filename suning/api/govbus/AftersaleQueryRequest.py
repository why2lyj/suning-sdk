# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class AftersaleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.skus = None
        
        self.setParamRule({
        	'cityId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryAftersale'

    def getApiMethod(self):

        return 'suning.govbus.aftersale.query'



