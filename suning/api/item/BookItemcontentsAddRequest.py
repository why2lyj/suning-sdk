# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookItemcontentsAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.itemCode = None
        self.afterSaleServiceDec = None
        self.saleSet = None
        self.invQty = None
        self.alertQty = None
        self.price = None
        self.freightTemplateId = None
        self.sellPoint = None                self.saleDate = None
        self.cmTitle = None                self.supplierImg1Url = None                self.supplierImg2Url = None                self.supplierImg3Url = None                self.supplierImg4Url = None                self.supplierImg5Url = None
    def getApiBizName(self):
        return 'itemContents'

    def getApiMethod(self):
        return 'suning.custom.book.itemcontents.add'

