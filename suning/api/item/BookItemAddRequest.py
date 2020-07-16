# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookItemAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invQty = None
        self.saleCatalogCode = None
        self.price = None
        self.brandCode = None
        self.productName = None
        self.itemCode = None
        self.categoryCode = None
        self.pars = None
        self.freightTemplateId = None
        self.saleSet = None
        self.sellPoint = None
        self.afterSaleServiceDec = None
        self.img1Url = None                self.img2Url = None                self.img3Url = None                self.img4Url = None                self.img5Url = None                self.cmTitle = None                self.supplierImg1Url = None                self.supplierImg2Url = None                self.supplierImg3Url = None                self.supplierImg4Url = None                self.supplierImg5Url = None
        self.saleDate = None
        self.alertQty = None                #：表示审核。商品系统中已存在此商品，继续发布新商品，需要审核。         self.auditFlag = None

    def getApiBizName(self):
        return 'item'

    def getApiMethod(self):
        return 'suning.custom.book.item.add'

