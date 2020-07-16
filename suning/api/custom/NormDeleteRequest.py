# -*- coding: utf-8 -*-

'''

Created on 2018-6-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class NormDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.valueItem = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'deleteNorm'

    def getApiMethod(self):

        return 'suning.custom.norm.delete'



