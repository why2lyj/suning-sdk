# -*- coding: utf-8 -*-

'''

Created on 2018-8-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class PrebindcardCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.systemNo = None
        self.transactionID = None
        self.opId = None
        self.orgId = None
        self.regionCode = None
        self.countyCode = None
        self.channelCode = None
        self.phoneNumber = None
        self.custName = None
        self.idType = None
        self.idCardNum = None
        self.address = None
        self.contractPhone = None
        
        self.setParamRule({
        	'systemNo':{'allow_empty':False},
        	'transactionID':{'allow_empty':False},
        	'opId':{'allow_empty':False},
        	'orgId':{'allow_empty':False},
        	'regionCode':{'allow_empty':False},
        	'countyCode':{'allow_empty':False},
        	'channelCode':{'allow_empty':False},
        	'phoneNumber':{'allow_empty':False},
        	'custName':{'allow_empty':False},
        	'idType':{'allow_empty':False},
        	'idCardNum':{'allow_empty':False},
        	'address':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createPrebindcard'

    def getApiMethod(self):

        return 'suning.operasale.prebindcard.create'



