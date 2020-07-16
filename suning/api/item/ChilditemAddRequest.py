# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ChilditemAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invQty = None
        self.price = None
        self.barcode = None
        self.itemCode = None
        self.pars = None
        self.parentProductCode = None
        self.img1Url = None
        self.img2Url = None
        self.img3Url = None                self.img4Url = None                self.img5Url = None
        self.alertQty = None
        self.supplierImg1Url = None                self.supplierImg2Url = None                self.supplierImg3Url = None                self.supplierImg4Url = None                self.supplierImg5Url = None
    def getApiBizName(self):
        return 'childItem'

    def getApiMethod(self):
        return 'suning.custom.childitem.add'

