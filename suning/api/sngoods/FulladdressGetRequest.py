# -*- coding: utf-8 -*-

'''

Created on 2020-5-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class FulladdressGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getFulladdress'

    def getApiMethod(self):

        return 'suning.sngoods.fulladdress.get'



