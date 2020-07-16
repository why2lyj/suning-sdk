# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class FouritemlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryFouritemlist'

    def getApiMethod(self):

        return 'suning.market.fouritemlist.query'



