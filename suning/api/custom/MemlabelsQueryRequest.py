# -*- coding: utf-8 -*-

'''

Created on 2018-9-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class MemlabelsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        self.laberCodes = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryMemlabels'

    def getApiMethod(self):

        return 'suning.custom.memlabels.query'



