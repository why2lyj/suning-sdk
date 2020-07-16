# -*- coding: utf-8 -*-

'''

Created on 2017-4-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class SingleinventoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invCode = None
        self.productCode = None
        
        self.setParamRule({
        	'invCode':{'allow_empty':False},
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSingleinventory'

    def getApiMethod(self):

        return 'suning.custom.singleinventory.get'



