# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PublishModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmTitle = None
        self.conventionBeginTime = None
        self.conventionEndTime = None
        self.conventionPoints = None
        self.detailModule = None
        self.endTime = None
        self.highBeginTime = None
        self.highEndTime = None
        self.highPoints = None
        self.introduction = None
        self.itemCode = None
        self.mobilePromotionLink = None
        self.packingList = None
        self.productCode = None
        self.promotionFlag = None
        self.promotionLink = None
        self.promotionPoints = None
        self.sellingPoints = None
        self.startTime = None
        self.supplierImgUrl = None
        self.videoCode = None
        self.mainPicVideoCode = None
        self.highlightWordone = None
        self.highlightWordtwo = None
        self.highlightWordthree = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyPublish'

    def getApiMethod(self):

        return 'suning.selfmarket.publish.modify'



