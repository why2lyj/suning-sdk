# -*- coding: utf-8 -*-

'''

Created on 2014-7-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MainproductGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyCode = None



    def getApiBizName(self):

        return 'mainProduct'



    def getApiMethod(self):

        return 'suning.custom.mainproduct.get'



