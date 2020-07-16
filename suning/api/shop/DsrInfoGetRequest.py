# -*- coding: utf-8 -*-

'''

Created on 2016-5-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class DsrInfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getDsrInfo'

    def getApiMethod(self):

        return 'suning.custom.dsrinfo.get'



