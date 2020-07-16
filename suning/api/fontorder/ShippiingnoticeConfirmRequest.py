# -*- coding: utf-8 -*-

'''

Created on 2017-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShippiingnoticeConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.attachStatus = None
        self.itemId = None
        self.orderCode = None
        self.rejectReason = None
        
        self.setParamRule({
        	'attachStatus':{'allow_empty':False},
        	'itemId':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'rejectReason':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmShippiingnotice'

    def getApiMethod(self):

        return 'suning.fontorder.shippiingnotice.confirm'



