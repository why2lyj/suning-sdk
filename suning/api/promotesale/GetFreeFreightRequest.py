# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetFreeFreightRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.freeFreightId = None



    def getApiBizName(self):

        return 'getFreeFreight'



    def getApiMethod(self):

        return 'suning.custom.freefreightdetail.get'



