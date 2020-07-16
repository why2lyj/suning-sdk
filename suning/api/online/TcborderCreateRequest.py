# -*- coding: utf-8 -*-

'''

Created on 2019-4-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class TcborderCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chanId = None
        self.orderId = None
        self.receiverAddress = None
        self.receiverCity = None
        self.receiverCounty = None
        self.receiverMobile = None
        self.receiverName = None
        self.receiverNationality = None
        self.receiverPhone = None
        self.receiverProvince = None
        self.receiverStreet = None
        self.receiverZip = None
        self.tcbOrderItemList = None
        self.totalFee = None
        self.totalNo = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'receiverAddress':{'allow_empty':False},
        	'receiverCity':{'allow_empty':False},
        	'receiverCounty':{'allow_empty':False},
        	'receiverMobile':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	'receiverProvince':{'allow_empty':False},
        	'totalFee':{'allow_empty':False},
        	'totalNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createTcborder'

    def getApiMethod(self):

        return 'suning.online.tcborder.create'



