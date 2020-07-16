# -*- coding: utf-8 -*-

'''

Created on 2014-7-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MainproductModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.correctParams = None



    def getApiBizName(self):

        return 'errCorreCont'



    def getApiMethod(self):

        return 'suning.custom.mainproduct.modify'



