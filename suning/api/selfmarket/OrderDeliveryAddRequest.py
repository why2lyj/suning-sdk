# -*- coding: utf-8 -*-

'''

Created on 2015-12-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDeliveryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.outOrderId = None
        self.orderSource = None
        self.scheduleType = None
        self.deliveryType = None
        self.scheduleDay = None
        self.scheduleStart = None
        self.scheduleEnd = None
        self.receiverZipCode = None
        self.receiverProvince = None
        self.receiverCity = None
        self.receiverArea = None
        self.receiverTown = None
        self.receiverAddress = None
        self.receiverName = None
        self.receiverMobile = None
        self.receiverPhone = None
        self.carCode = None
        self.orderFlag = None
        self.custSelectNumber = None
        self.orderProductList = None
        
        self.setParamRule({
        	'outOrderId':{'allow_empty':False},
        	'orderSource':{'allow_empty':False},
        	'receiverProvince':{'allow_empty':False},
        	'receiverCity':{'allow_empty':False},
        	'receiverArea':{'allow_empty':False},
        	'receiverTown':{'allow_empty':False},
        	'receiverAddress':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addOrderDelivery'

    def getApiMethod(self):

        return 'suning.fourps.orderdelivery.add'



