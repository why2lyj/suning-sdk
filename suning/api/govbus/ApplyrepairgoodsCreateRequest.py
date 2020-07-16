# -*- coding: utf-8 -*-

'''

Created on 2019-6-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplyrepairgoodsCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.cityId = None
        self.countyId = None
        self.mobPhoneNum = None
        self.num = None
        self.orderId = None
        self.orderItemId = None
        self.orderMemo = None
        self.phoneNum = None
        self.provinceId = None
        self.receiverName = None
        self.serviceTime = None
        self.skuId = None
        self.srvMemo = None
        self.townId = None
        
        self.setParamRule({
        	'address':{'allow_empty':False},
        	'cityId':{'allow_empty':False},
        	'countyId':{'allow_empty':False},
        	'mobPhoneNum':{'allow_empty':False},
        	'num':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'orderMemo':{'allow_empty':False},
        	'provinceId':{'allow_empty':False},
        	'receiverName':{'allow_empty':False},
        	'serviceTime':{'allow_empty':False},
        	'skuId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createApplyrepairgoods'

    def getApiMethod(self):

        return 'suning.govbus.applyrepairgoods.create'



