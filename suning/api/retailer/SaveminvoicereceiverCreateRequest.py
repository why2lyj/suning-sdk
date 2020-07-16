# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaveminvoicereceiverCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cityCode = None
        self.cityName = None
        self.contactPerson = None
        self.contactPhone = None
        self.createTime = None
        self.createUser = None
        self.detailAddress = None
        self.districtCode = None
        self.districtName = None
        self.merchantCode = None
        self.provCode = None
        self.provName = None
        self.townCode = None
        self.townName = None
        self.updateTime = None
        self.updateUser = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createSaveminvoicereceiver'

    def getApiMethod(self):

        return 'suning.retailer.saveminvoicereceiver.create'



