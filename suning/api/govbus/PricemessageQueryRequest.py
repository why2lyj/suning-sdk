# -*- coding: utf-8 -*-

'''

Created on 2017-11-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class PricemessageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryPricemessage'

    def getApiMethod(self):

        return 'suning.govbus.pricemessage.query'



