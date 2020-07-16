# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReserveQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appointmentOrder = None
        self.endPlannedArrivalDate = None
        self.endUpdateTime = None
        self.orderCode = None
        self.startPlannedArrivalDate = None
        self.startUpdateTime = None
        self.wayBillOrder = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'reserveQuery'

    def getApiMethod(self):

        return 'suning.selfmarket.reserve.query'



