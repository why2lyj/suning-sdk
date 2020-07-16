# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class MemberstoreregistrationCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.cityCode = None
        self.cityName = None
        self.companyAddr = None
        self.companyName = None
        self.companyType = None
        self.contactPerson = None
        self.contactPhone = None
        self.districtCode = None
        self.districtName = None
        self.legalIdcardNo = None
        self.legalPerson = None
        self.licenseNo = None
        self.merchantType = None
        self.provCode = None
        self.provName = None
        self.townCode = None
        self.townName = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'channelCode':{'allow_empty':False},
        	'cityCode':{'allow_empty':False},
        	'cityName':{'allow_empty':False},
        	'companyAddr':{'allow_empty':False},
        	'companyName':{'allow_empty':False},
        	'companyType':{'allow_empty':False},
        	'contactPerson':{'allow_empty':False},
        	'contactPhone':{'allow_empty':False},
        	'districtCode':{'allow_empty':False},
        	'districtName':{'allow_empty':False},
        	'merchantType':{'allow_empty':False},
        	'provCode':{'allow_empty':False},
        	'provName':{'allow_empty':False},
        	'townCode':{'allow_empty':False},
        	'townName':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createMemberstoreregistration'

    def getApiMethod(self):

        return 'suning.retailer.memberstoreregistration.create'



