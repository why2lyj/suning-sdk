# -*- coding: utf-8 -*-

'''

Created on 2019-6-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class PrivatememsceneQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPrivatememscene'

    def getApiMethod(self):

        return 'suning.market.privatememscene.query'



