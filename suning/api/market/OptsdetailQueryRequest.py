# -*- coding: utf-8 -*-

'''

Created on 2020-1-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class OptsdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOptsdetail'

    def getApiMethod(self):

        return 'suning.market.optsdetail.query'



