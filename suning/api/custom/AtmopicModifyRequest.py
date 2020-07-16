# -*- coding: utf-8 -*-

'''

Created on 2019-4-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class AtmopicModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.atmoPicInfo = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyAtmopic'

    def getApiMethod(self):

        return 'suning.custom.atmopic.modify'



