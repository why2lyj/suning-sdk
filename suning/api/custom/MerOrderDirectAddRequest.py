# -*- coding: utf-8 -*-

'''

Created on 2017-12-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class MerOrderDirectAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityCode = None
        self.cmmdtyQaType = None
        self.consignee = None
        self.extdCmmdtyBand = None
        self.extdCmmdtyCtgry = None
        self.extdCommodityCode = None
        self.extdCommodityName = None
        self.faultTypeCode = None
        self.mobPhoneNum = None
        self.orderChannel = None
        self.orderTime = None
        self.phoneNum = None
        self.proName = None
        self.saleDate = None
        self.saleQty = None
        self.salesPerson = None
        self.sapOrderType = None
        self.serviceTime = None
        self.sourceOrderItemId = None
        self.srvAddress = None
        self.srvAreaCode = None
        self.srvMemo = None
        
        self.setParamRule({
        	'cityCode':{'allow_empty':False},
        	'cmmdtyQaType':{'allow_empty':False},
        	'consignee':{'allow_empty':False},
        	'extdCmmdtyBand':{'allow_empty':False},
        	'extdCmmdtyCtgry':{'allow_empty':False},
        	'extdCommodityName':{'allow_empty':False},
        	'mobPhoneNum':{'allow_empty':False},
        	'orderChannel':{'allow_empty':False},
        	'orderTime':{'allow_empty':False},
        	'proName':{'allow_empty':False},
        	'saleDate':{'allow_empty':False},
        	'saleQty':{'allow_empty':False},
        	'salesPerson':{'allow_empty':False},
        	'sapOrderType':{'allow_empty':False},
        	'serviceTime':{'allow_empty':False},
        	'sourceOrderItemId':{'allow_empty':False},
        	'srvAddress':{'allow_empty':False},
        	'srvAreaCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addMerOrderDirect'

    def getApiMethod(self):

        return 'suning.custom.merorderdirect.add'



