# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReservesupplierQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appointmentOrder = None
        self.endPlannedArrivalDate = None
        self.endUpdateTime = None
        self.orderCode = None
        self.pageNo = None
        self.pageSize = None
        self.startPlannedArrivalDate = None
        self.startUpdateTime = None
        self.supplierCode = None
        self.wayBillOrder = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryReservesupplier'

    def getApiMethod(self):

        return 'suning.selfmarket.reservesupplier.query'



