# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CulitemcontentsModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.afterSaleServiceDec = None
        self.alertQty = None
        self.assortCode = None
        self.cmTitle = None
        self.detailModule = None
        self.freightTemplateId = None
        self.highlightWordone = None
        self.highlightWordthree = None
        self.highlightWordtwo = None
        self.introduction = None
        self.invQty = None
        self.itemCode = None
        self.mainPicVideoCode = None
        self.price = None
        self.productCode = None
        self.saleDate = None
        self.saleSet = None
        self.sellPoint = None
        self.supplierImgAUrl = None
        self.supplierImgBUrl = None
        self.supplierImgCUrl = None
        self.supplierImgDUrl = None
        self.supplierImgEUrl = None
        
        self.setParamRule({
        	'afterSaleServiceDec':{'allow_empty':False},
        	'cmTitle':{'allow_empty':False},
        	'freightTemplateId':{'allow_empty':False},
        	'invQty':{'allow_empty':False},
        	'itemCode':{'allow_empty':False},
        	'price':{'allow_empty':False},
        	'productCode':{'allow_empty':False},
        	'saleSet':{'allow_empty':False},
        	'supplierImgAUrl':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyCulitemcontents'

    def getApiMethod(self):

        return 'suning.custom.culitemcontents.modify'



