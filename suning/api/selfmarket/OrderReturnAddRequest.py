# -*- coding: utf-8 -*-

'''

Created on 2015-12-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderReturnAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.outOrderId = None
        self.oldOrderId = None
        self.orderSource = None
        self.expectStartTime = None
        self.expectEndTime = None
        self.remark = None
        self.senderZipCode = None
        self.senderProvince = None
        self.senderCity = None
        self.senderArea = None
        self.senderTown = None
        self.senderAddress = None
        self.senderName = None
        self.senderMobile = None
        self.senderPhone = None
        self.takeFlag = None
        self.orderFlag = None
        self.orderProductList = None
        
        self.setParamRule({
        	'outOrderId':{'allow_empty':False},
        	'oldOrderId':{'allow_empty':False},
        	'orderSource':{'allow_empty':False},
        	'expectStartTime':{'allow_empty':False},
        	'expectEndTime':{'allow_empty':False},
        	'senderProvince':{'allow_empty':False},
        	'senderCity':{'allow_empty':False},
        	'senderName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addOrderReturn'

    def getApiMethod(self):

        return 'suning.fourps.orderreturn.add'



