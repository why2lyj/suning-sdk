# -*- coding: utf-8 -*-

'''

Created on 2018-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReceiveinfoModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityName = None
        self.customerName = None
        self.detailAddress = None
        self.districtName = None
        self.mobilePhoneNum = None
        self.orderCode = None
        self.phoneNum = None
        self.provinceName = None
        self.supplierCode = None
        self.townCode = None
        self.townName = None
        self.userName = None
        
        self.setParamRule({
        	'cityName':{'allow_empty':False},
        	'customerName':{'allow_empty':False},
        	'detailAddress':{'allow_empty':False},
        	'districtName':{'allow_empty':False},
        	'mobilePhoneNum':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'provinceName':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	'townCode':{'allow_empty':False},
        	'townName':{'allow_empty':False},
        	'userName':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyReceiveinfo'

    def getApiMethod(self):

        return 'suning.selfmarket.receiveinfo.modify'



