# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class DicsingleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.banktypecode = None
        self.operType = None
        self.payCode = None
        
        self.setParamRule({
        	'operType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryDicsingle'

    def getApiMethod(self):

        return 'suning.custom.dicsingle.query'



