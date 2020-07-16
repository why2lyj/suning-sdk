# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChargeItemInfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.serverId = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getChargeItemInfo'

    def getApiMethod(self):

        return 'suning.fws.chargeiteminfo.get'



