# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class BoorderUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateBoorder'

    def getApiMethod(self):

        return 'suning.online.boorder.update'



