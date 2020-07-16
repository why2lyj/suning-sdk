# -*- coding: utf-8 -*-

'''

Created on 2018-8-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class CreateuserfeeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelCode = None
        self.productId = None
        
        self.setParamRule({
        	'channelCode':{'allow_empty':False},
        	'productId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCreateuserfee'

    def getApiMethod(self):

        return 'suning.operasale.createuserfee.get'



