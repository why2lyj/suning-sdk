# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class DispatchOrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderSource = None
        self.sourceOrderItemId = None
        self.orderType = None
        self.orderTime = None
        self.saleQty = None
        self.cmmdtyQaType = None
        self.serviceTime = None
        self.extdCmmdtyBand = None
        self.extdCmmdtyCtgry = None
        self.extdCommodityName = None
        self.consignee = None
        self.phoneNum = None
        self.mobPhoneNum = None
        self.srvAddress = None
        self.standardCode = None
        self.cityCode = None
        self.srvAreaCode = None
        self.srvMemo = None
        self.saleDate = None
        self.serviceSource = None
        self.salesPerson = None
        self.orderChannel = None
        self.faultTypeCode = None
        self.customerProperty = None
        
        self.setParamRule({
        	'orderSource':{'allow_empty':False},
        	'sourceOrderItemId':{'allow_empty':False},
        	'orderType':{'allow_empty':False},
        	'orderTime':{'allow_empty':False},
        	'saleQty':{'allow_empty':False},
        	'cmmdtyQaType':{'allow_empty':False},
        	'extdCmmdtyBand':{'allow_empty':False},
        	'extdCmmdtyCtgry':{'allow_empty':False},
        	'consignee':{'allow_empty':False},
        	'mobPhoneNum':{'allow_empty':False},
        	'srvAddress':{'allow_empty':False},
        	'standardCode':{'allow_empty':False},
        	'salesPerson':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addDispatchOrder'

    def getApiMethod(self):

        return 'suning.asmp.dispatchorder.add'



