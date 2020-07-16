# -*- coding: utf-8 -*-

'''

Created on 2020-6-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class PxcardstatusReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.deliveryDate = None
        self.expressCompanyCode = None
        self.expressNo = None
        self.name = None
        self.orderItemId = None
        self.phoneNum = None
        self.pickupMode = None
        self.pxCardId = None
        self.pxCardNo = None
        self.pxCardStatus = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False},
        	'pickupMode':{'allow_empty':False},
        	'pxCardId':{'allow_empty':False},
        	'pxCardNo':{'allow_empty':False},
        	'pxCardStatus':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receivePxcardstatus'

    def getApiMethod(self):

        return 'suning.custom.pxcardstatus.receive'



