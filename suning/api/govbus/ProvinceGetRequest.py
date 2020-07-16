# -*- coding: utf-8 -*-

'''

Created on 2020-6-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProvinceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getProvince'

    def getApiMethod(self):

        return 'suning.govbus.province.get'



