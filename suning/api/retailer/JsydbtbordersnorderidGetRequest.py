# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydbtbordersnorderidGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.thirdOrder = None
        self.token = None
        
        self.setParamRule({
        	'thirdOrder':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getJsydbtbordersnorderid'

    def getApiMethod(self):

        return 'suning.retailer.jsydbtbordersnorderid.get'



