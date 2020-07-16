# -*- coding: utf-8 -*-

'''

Created on 2017-4-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SNServiceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.awardFee = None
        self.basicFee = None
        self.chargbakCode = None
        self.chargbakReson = None
        self.custName = None
        self.inputFee = None
        self.installedId = None
        self.itemGuId = None
        self.longDistanceFee = None
        self.orderStatus = None
        self.otherFee = None
        self.recordGuId = None
        self.settlementId = None
        self.srvOrdId = None
        self.srvOrdType = None
        self.telNoFir = None
        self.telNoSec = None
        self.verifyCode = None
        self.verifyMsg = None
        
        self.setParamRule({
        	'installedId':{'allow_empty':False},
        	'itemGuId':{'allow_empty':False},
        	'orderStatus':{'allow_empty':False},
        	'recordGuId':{'allow_empty':False},
        	'srvOrdId':{'allow_empty':False},
        	'srvOrdType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'snserviceadd'

    def getApiMethod(self):

        return 'suning.selfmarket.snservice.add'



