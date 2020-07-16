# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class VirtualGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemCode = None
        
        self.setParamRule({
        	'orderItemCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getVirtual'

    def getApiMethod(self):

        return 'suning.custom.virtual.get'



