# -*- coding: utf-8 -*-

'''

Created on 2017-11-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderpackageAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderPackage = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addOrderpackage'

    def getApiMethod(self):

        return 'suning.selfmarket.orderpackage.add'



