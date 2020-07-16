# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsOutsourceTaskGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.logisticOrderId = None



    def getApiBizName(self):

        return 'getLogisticsOutsourceTask'



    def getApiMethod(self):

        return 'suning.logistics.outsourcetask.get'



