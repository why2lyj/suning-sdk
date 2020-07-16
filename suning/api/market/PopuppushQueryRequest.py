# -*- coding: utf-8 -*-

'''

Created on 2020-1-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PopuppushQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPopuppush'

    def getApiMethod(self):

        return 'suning.market.popuppush.query'



