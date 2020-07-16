# -*- coding: utf-8 -*-

'''

Created on 2020-4-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class itemContentsAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.afterSaleServiceDec = None
        self.alertQty = None
        self.assortCode = None
        self.autoRefund = None
        self.bookingShop = None
        self.childItem = None
        self.cmTitle = None
        self.deductiblePrice = None
        self.detailModule = None
        self.effectiveDay = None
        self.extractMode = None
        self.insaleRefund = None
        self.introduction = None
        self.invQty = None
        self.itemCode = None
        self.mobile = None
        self.mobileNew = None
        self.packingList = None
        self.payTemplate = None
        self.peopleNum = None
        self.pingouPrice = None
        self.price = None
        self.priceType = None
        self.productCode = None
        self.purchaseMin = None
        self.saleDate = None
        self.saleSet = None
        self.sellChannel = None
        self.sellPoint = None
        self.sourceCountry = None
        self.supplierImg10Url = None
        self.supplierImg1Url = None
        self.supplierImg2Url = None
        self.supplierImg3Url = None
        self.supplierImg4Url = None
        self.supplierImg5Url = None
        self.supplierImg6Url = None
        self.supplierImg7Url = None
        self.supplierImg8Url = None
        self.supplierImg9Url = None
        self.writeoffPayment = None
        self.writeoffShop = None
        
        self.setParamRule({
        	'cmTitle':{'allow_empty':False},
        	'peopleNum':{'allow_empty':False},
        	'pingouPrice':{'allow_empty':False},
        	'productCode':{'allow_empty':False},
        	'purchaseMin':{'allow_empty':False},
        	'saleSet':{'allow_empty':False},
        	'supplierImg1Url':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'itemContents'

    def getApiMethod(self):

        return 'suning.integrate.itemcontents.add'



