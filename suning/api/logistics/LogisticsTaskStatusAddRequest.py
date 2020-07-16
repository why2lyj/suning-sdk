# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsTaskStatusAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.logisticOrderId = None
        self.logisticExpressId = None
        self.logisticStation = None
        self.state = None
        self.finishedDate = None
        self.finishedTime = None
        self.consignee = None
        self.operator = None
        self.telNumber = None
        self.shipmentCode = None
        self.weight = None
        self.weightUnit = None
        self.note = None
        self.airwayBillNo = None
        self.flightDate = None
        self.flightNo = None



    def getApiBizName(self):

        return 'addLogisticsTaskStatus'



    def getApiMethod(self):

        return 'suning.logistics.taskstatusfeedback.add'



