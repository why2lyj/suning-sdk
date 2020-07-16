# -*- coding: utf-8 -*-

'''

Created on 2017-3-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceExclusiveGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPriceExclusive'

    def getApiMethod(self):

        return 'suning.custom.priceexclusive.get'



