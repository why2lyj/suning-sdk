# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class FeaturewordModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.featureWordOne = None
        self.productCode = None
        self.featureWordTwo = None
        self.featureWordThree = None
        
        self.setParamRule({
        	'featureWordOne':{'allow_empty':False},
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyFeatureword'

    def getApiMethod(self):

        return 'suning.custom.featureword.modify'



