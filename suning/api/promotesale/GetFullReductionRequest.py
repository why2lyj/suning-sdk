# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetFullReductionRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.fullReductionId = None



    def getApiBizName(self):

        return 'getFullReduction'



    def getApiMethod(self):

        return 'suning.custom.fullreductiondetail.get'



