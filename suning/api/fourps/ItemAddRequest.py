# -*- coding: utf-8 -*-

'''

Created on 2016-8-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCmCode = None
        self.productName = None
        self.gbCode = None
        self.cmLength = None
        self.cmWidth = None
        self.cmHeight = None
        self.cmVolume = None
        self.grossWeight = None
        self.netWeight = None
        self.shelfLifeFlag = None
        self.shelfLife = None
        self.packingList = None
        self.categoryName1 = None
        self.categoryName2 = None
        self.brandName = None
        self.standard = None
        self.model = None
        self.categoryCode = None
        self.brandCode = None
        self.cmType = None
        self.cmTitle = None
        self.cmArea = None
        
        self.setParamRule({
        	'supplierCmCode':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	'cmVolume':{'allow_empty':False},
        	'grossWeight':{'allow_empty':False},
        	'shelfLifeFlag':{'allow_empty':False},
        	'categoryCode':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	'cmType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addItem'

    def getApiMethod(self):

        return 'suning.fourps.item.add'



