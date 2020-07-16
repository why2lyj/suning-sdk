# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class MainproductGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.correctId = None
        
        self.setParamRule({
        	'correctId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getMainproduct'

    def getApiMethod(self):

        return 'suning.saleoff.mainproduct.get'



