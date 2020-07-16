# -*- coding: utf-8 -*-

'''

Created on 2020-4-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class invaddressQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'invaddress'

    def getApiMethod(self):

        return 'suning.custom.invaddress.query'



