# -*- coding: utf-8 -*-

'''

Created on 2018-12-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class LeaguerstatusAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.iqStatus = None
        self.orderId = None
        self.orderItemId = None
        self.supplierCode = None
        
        self.setParamRule({
        	'iqStatus':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addLeaguerstatus'

    def getApiMethod(self):

        return 'suning.selfmarket.leaguerstatus.add'



