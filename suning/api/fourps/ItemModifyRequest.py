# -*- coding: utf-8 -*-

'''

Created on 2016-8-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemModifyRequest(AbstractApi):

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
        self.packingList = None
        self.shelfLife = None
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
        	'productName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyItem'

    def getApiMethod(self):

        return 'suning.fourps.item.modify'



