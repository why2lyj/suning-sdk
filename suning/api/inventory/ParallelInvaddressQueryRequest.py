# -*- coding: utf-8 -*-

'''

Created on 2016-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class ParallelInvaddressQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryParallelInvaddress'

    def getApiMethod(self):

        return 'suning.custom.parallelinvaddress.query'



