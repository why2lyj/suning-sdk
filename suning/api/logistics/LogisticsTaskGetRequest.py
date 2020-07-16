# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsTaskGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.ladingBill = None



    def getApiBizName(self):

        return 'getLogisticsTask'



    def getApiMethod(self):

        return 'suning.logistics.task.get'



