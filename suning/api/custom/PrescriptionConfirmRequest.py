# -*- coding: utf-8 -*-

'''

Created on 2020-4-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class PrescriptionConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.msg = None
        self.orderId = None
        self.orderItemId = None
        self.picUrl = None
        self.reviewResult = None
        self.supplierCode = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'reviewResult':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmPrescription'

    def getApiMethod(self):

        return 'suning.custom.prescription.confirm'



