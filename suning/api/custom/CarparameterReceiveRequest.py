# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class CarparameterReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.modelSlug = None
        self.productCode = None
        
        self.setParamRule({
        	'modelSlug':{'allow_empty':False},
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveCarparameter'

    def getApiMethod(self):

        return 'suning.custom.carparameter.receive'



