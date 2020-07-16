# -*- coding: utf-8 -*-

'''

Created on 2020-4-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class prescriptionParamsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderInfo = None
        self.supplierInfo = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'prescriptionParams'

    def getApiMethod(self):

        return 'suning.custom.prescriptionorder.query'



