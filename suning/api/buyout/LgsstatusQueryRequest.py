# -*- coding: utf-8 -*-

'''

Created on 2019-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class LgsstatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLgsstatus'

    def getApiMethod(self):

        return 'suning.buyout.lgsstatus.query'



