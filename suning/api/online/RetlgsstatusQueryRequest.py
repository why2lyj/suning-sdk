# -*- coding: utf-8 -*-

'''

Created on 2018-9-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class RetlgsstatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRetlgsstatus'

    def getApiMethod(self):

        return 'suning.online.retlgsstatus.query'



