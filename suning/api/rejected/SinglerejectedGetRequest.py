# -*- coding: utf-8 -*-

'''

Created on 2018-5-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class SinglerejectedGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'singleGetRejected'

    def getApiMethod(self):

        return 'suning.custom.singlerejected.get'



