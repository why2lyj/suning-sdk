# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class SoaUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateSoaupdate'

    def getApiMethod(self):

        return 'suning.market.soaupdate.update'



