# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class TmallinventoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryTmallinventory'

    def getApiMethod(self):

        return 'suning.selfmarket.tmallinventory.query'



