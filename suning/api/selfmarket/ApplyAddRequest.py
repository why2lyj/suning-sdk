# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplyAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.barpic = None
        self.brandCode = None
        self.categoryCode = None
        self.childItem = None
        self.cmTitle = None
        self.conventionBeginTime = None
        self.conventionEndTime = None
        self.conventionPoints = None
        self.detailModule = None
        self.endTime = None
        self.highBeginTime = None
        self.highEndTime = None
        self.highlightWordone = None
        self.highlightWordthree = None
        self.highlightWordtwo = None
        self.highPoints = None
        self.introduction = None
        self.itemCode = None
        self.mainPicVideoCode = None
        self.mobilePromotionLink = None
        self.packingList = None
        self.pars = None
        self.productName = None
        self.promotionFlag = None
        self.promotionLink = None
        self.promotionPoints = None
        self.sellingPoints = None
        self.startTime = None
        self.supplierImgUrl = None
        self.videoCode = None
        
        self.setParamRule({
        	'brandCode':{'allow_empty':False},
        	'categoryCode':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addApply'

    def getApiMethod(self):

        return 'suning.selfmarket.apply.add'



