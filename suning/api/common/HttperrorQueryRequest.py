# -*- coding: utf-8 -*-

'''

Created on 2020-3-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class HttperrorQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.aaa = None
        self.bbb = None
        
        self.setParamRule({
        	'aaa':{'allow_empty':False},
        	'bbb':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryHttperror'

    def getApiMethod(self):

        return 'suning.common.httperror.query'



