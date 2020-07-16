# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class RealCelStorageGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appointOrderId = None
        self.purchaseOrderId = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getRealCelStorage'

    def getApiMethod(self):

        return 'suning.fourps.realcelstorage.get'



