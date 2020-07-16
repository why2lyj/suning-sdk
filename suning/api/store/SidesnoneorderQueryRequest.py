# -*- coding: utf-8 -*-

'''

Created on 2019-12-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnoneorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySidesnoneorder'

    def getApiMethod(self):

        return 'suning.store.sidesnoneorder.query'



