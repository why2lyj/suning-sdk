# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class CarmodelQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.nkId = None
        
        self.setParamRule({
        	'nkId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCarmodel'

    def getApiMethod(self):

        return 'suning.custom.carmodel.query'



