# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommodityeditCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.advertise = None
        self.applyCode = None
        self.appStoreCode = None
        self.attrInfo = None
        self.brandCode = None
        self.brgew = None
        self.categoryCode = None
        self.classifyCode = None
        self.cmBarcode = None
        self.deliveryAttr = None
        self.immediateAppoint = None
        self.immediateAppointTime = None
        self.operType = None
        self.packingPrice = None
        self.picUrl = None
        self.productCode = None
        self.productName = None
        self.purchaseMin = None
        self.qty = None
        self.secondClassifyCode = None
        self.sellHoursType = None
        self.sellPrice = None
        self.sellStatus = None
        self.serviceTime = None
        self.standardInfo = None
        self.storeCode = None
        self.supplierCmCode = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	'classifyCode':{'allow_empty':False},
        	'operType':{'allow_empty':False},
        	'picUrl':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	'purchaseMin':{'allow_empty':False},
        	'qty':{'allow_empty':False},
        	'sellHoursType':{'allow_empty':False},
        	'sellPrice':{'allow_empty':False},
        	'sellStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createCommodityedit'

    def getApiMethod(self):

        return 'suning.store.commodityedit.create'



