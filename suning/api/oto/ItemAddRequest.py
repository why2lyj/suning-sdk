# -*- coding: utf-8 -*-

'''

Created on 2016-11-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.brandCode = None
        self.productName = None
        self.sellPoint = None
        self.saleSet = None
        self.cmTitle = None
        self.targetChannel = None
        self.price = None
        self.itemCode = None
        self.assortCode = None
        self.supplierImg1Url = None
        self.supplierImg2Url = None
        self.supplierImg3Url = None
        self.supplierImg4Url = None
        self.supplierImg5Url = None
        self.pars = None
        self.childItem = None
        self.barpic = None
        self.introduction = None
        self.detailModule = None
        self.packingList = None
        self.saleDate = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addItem'

    def getApiMethod(self):

        return 'suning.oto.item.add'



