# -*- coding: utf-8 -*-

'''

Created on 2019-6-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class OptstranstitleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOptstranstitle'

    def getApiMethod(self):

        return 'suning.market.optstranstitle.query'



