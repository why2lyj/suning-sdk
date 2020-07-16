# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class PublishcmAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.assortCode = None
        self.childItem = None
        self.cmTitle = None
        self.detailModule = None
        self.introduction = None
        self.itemCode = None
        self.mainPicVideoCode = None
        self.packingList = None
        self.price = None
        self.productCode = None
        self.saleDate = None
        self.saleSet = None
        self.sellPoint = None
        self.supplierImg1Url = None
        self.supplierImg2Url = None
        self.supplierImg3Url = None
        self.supplierImg4Url = None
        self.supplierImg5Url = None
        self.targetChannel = None
        self.videoCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addPublishcm'

    def getApiMethod(self):

        return 'suning.oto.publishcm.add'



