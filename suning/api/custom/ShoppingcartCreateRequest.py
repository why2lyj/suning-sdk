# -*- coding: utf-8 -*-

'''

Created on 2020-5-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShoppingcartCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chan = None
        self.cmmdtyCode = None
        self.cmmdtyName = None
        self.cmmdtyQty = None
        self.operationEquipment = None
        self.operationTerminal = None
        self.overSeasFlag = None
        self.snUnionId = None
        self.tickStatus = None
        self.xzActivityId = None
        
        self.setParamRule({
        	'chan':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'cmmdtyName':{'allow_empty':False},
        	'cmmdtyQty':{'allow_empty':False},
        	'operationEquipment':{'allow_empty':False},
        	'operationTerminal':{'allow_empty':False},
        	'snUnionId':{'allow_empty':False},
        	'tickStatus':{'allow_empty':False},
        	'xzActivityId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createShoppingcart'

    def getApiMethod(self):

        return 'suning.custom.shoppingcart.create'



