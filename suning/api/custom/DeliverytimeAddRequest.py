# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class DeliverytimeAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.childCmList = None
        self.deliveryTime = None
        self.deliveryTimeType = None
        self.isStandardSet = None
        self.productCode = None
        self.supplierCode = None
        
        self.setParamRule({
        	'deliveryTimeType':{'allow_empty':False},
        	'productCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addDeliverytime'

    def getApiMethod(self):

        return 'suning.custom.deliverytime.add'



