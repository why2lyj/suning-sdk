# -*- coding: utf-8 -*-

'''

Created on 2014-12-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetLogisticsCrossbuyPrdCustDeclRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.logisticOrderId = None
        self.orderNo = None



    def getApiBizName(self):

        return 'getLogisticsCrossbuyPrdCustDecl'



    def getApiMethod(self):

        return 'suning.logistics.crossbuyprdcustdecl.get'



