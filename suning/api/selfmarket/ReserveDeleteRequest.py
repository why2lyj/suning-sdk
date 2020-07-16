# -*- coding: utf-8 -*-

'''

Created on 2017-9-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReserveDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appointmentOrder = None
        self.deliveryNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'deleteReserve'

    def getApiMethod(self):

        return 'suning.selfmarket.reserve.delete'



