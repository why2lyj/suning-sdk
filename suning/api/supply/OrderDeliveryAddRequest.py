# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDeliveryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.packageOrderId = None
        self.deliveryType = None
        self.expressCompanyCode = None
        self.expressNo = None
        
        self.setParamRule({
        	'packageOrderId':{'allow_empty':False},
        	'deliveryType':{'allow_empty':False},
        	'expressCompanyCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addOrderDelivery'

    def getApiMethod(self):

        return 'suning.supply.orderdelivery.add'



