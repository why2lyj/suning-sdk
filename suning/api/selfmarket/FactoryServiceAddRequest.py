# -*- coding: utf-8 -*-

'''

Created on 2016-4-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class FactoryServiceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.recordGuId = None
        self.itemGuId = None
        self.srvOrdId = None
        self.srvOrdType = None
        self.orderStatus = None
        self.facSiteName = None
        self.facSiteTel = None
        self.srvStatus = None
        self.inCompleteReason = None
        self.installedId = None
        
        self.setParamRule({
        	'recordGuId':{'allow_empty':False},
        	'itemGuId':{'allow_empty':False},
        	'srvOrdId':{'allow_empty':False},
        	'srvOrdType':{'allow_empty':False},
        	'orderStatus':{'allow_empty':False},
        	'srvStatus':{'allow_empty':False},
        	'installedId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'facserviceadd'

    def getApiMethod(self):

        return 'suning.facservice.add'



