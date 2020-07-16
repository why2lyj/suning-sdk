# -*- coding: utf-8 -*-

'''

Created on 2017-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class PublishcmAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.sellPoint = None
        self.cmTitle = None
        self.price = None
        self.itemCode = None
        self.introduction = None
        self.packingList = None
        self.childItem = None
        self.detailModule = None
        self.supplierImgUrlA = None
        self.supplierImgUrlB = None
        self.supplierImgUrlC = None
        self.supplierImgUrlD = None
        self.supplierImgUrlE = None
        self.ltpic = None
        self.afterSaleServiceDec = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'sellPoint':{'allow_empty':False},
        	'cmTitle':{'allow_empty':False},
        	'price':{'allow_empty':False},
        	'supplierImgUrlB':{'allow_empty':False},
        	'supplierImgUrlC':{'allow_empty':False},
        	'supplierImgUrlD':{'allow_empty':False},
        	'supplierImgUrlE':{'allow_empty':False},
        	'ltpic':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addPublishcm'

    def getApiMethod(self):

        return 'suning.saleoff.publishcm.add'



