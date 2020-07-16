# -*- coding: utf-8 -*-

'''

Created on 2018-12-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChanneluserCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.channelCode = None
        self.contractPhone = None
        self.countyCode = None
        self.custName = None
        self.fee = None
        self.iccid = None
        self.idCardNum = None
        self.idType = None
        self.imsi = None
        self.mainOfferId = None
        self.opId = None
        self.orgId = None
        self.phoneNumber = None
        self.regionCode = None
        self.systemNo = None
        self.transactionID = None
        
        self.setParamRule({
        	'address':{'allow_empty':False},
        	'channelCode':{'allow_empty':False},
        	'countyCode':{'allow_empty':False},
        	'custName':{'allow_empty':False},
        	'fee':{'allow_empty':False},
        	'iccid':{'allow_empty':False},
        	'idCardNum':{'allow_empty':False},
        	'idType':{'allow_empty':False},
        	'imsi':{'allow_empty':False},
        	'mainOfferId':{'allow_empty':False},
        	'opId':{'allow_empty':False},
        	'orgId':{'allow_empty':False},
        	'phoneNumber':{'allow_empty':False},
        	'regionCode':{'allow_empty':False},
        	'systemNo':{'allow_empty':False},
        	'transactionID':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createChanneluser'

    def getApiMethod(self):

        return 'suning.operasale.channeluser.create'



