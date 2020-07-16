# -*- coding: utf-8 -*-

'''

Created on 2020-3-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoordertrackQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOtoordertrack'

    def getApiMethod(self):

        return 'suning.onlinestore.ordertrack.query'



