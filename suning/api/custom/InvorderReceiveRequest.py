# -*- coding: utf-8 -*-

'''

Created on 2020-5-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvorderReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.buySign = None
        self.clientAddress = None
        self.clientBank = None
        self.clientBankNum = None
        self.clientEmail = None
        self.clientName = None
        self.clientPhone = None
        self.clientTaxNum = None
        self.clientTel = None
        self.clientType = None
        self.cmmdtys = None
        self.countMoney = None
        self.detialSign = None
        self.extendField = None
        self.howtoPrint = None
        self.oldTicketCode = None
        self.oldTicketNum = None
        self.orderNum = None
        self.orderNumPwd = None
        self.orderReturnNum = None
        self.orderTime = None
        self.payeeName = None
        self.platformCoding = None
        self.receiveMode = None
        self.remark = None
        self.reviwerName = None
        self.saleAddress = None
        self.saleBank = None
        self.saleBankNum = None
        self.saleName = None
        self.saleTaxNum = None
        self.saleTel = None
        self.specialRedSign = None
        self.sysSource = None
        self.ticketName = None
        self.ticketType = None
        
        self.setParamRule({
        	'countMoney':{'allow_empty':False},
        	'detialSign':{'allow_empty':False},
        	'orderNum':{'allow_empty':False},
        	'orderTime':{'allow_empty':False},
        	'platformCoding':{'allow_empty':False},
        	'saleTaxNum':{'allow_empty':False},
        	'ticketType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveInvorder'

    def getApiMethod(self):

        return 'suning.custom.invorder.receive'



