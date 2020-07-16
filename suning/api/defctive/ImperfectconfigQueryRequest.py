# -*- coding: utf-8 -*-

'''

Created on 2020-4-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class ImperfectconfigQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.buCode = None
        self.serialNum = None
        
        self.setParamRule({
        	'serialNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryImperfectconfig'

    def getApiMethod(self):

        return 'suning.defctive.imperfectconfig.query'



