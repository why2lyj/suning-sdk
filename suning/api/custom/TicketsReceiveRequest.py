# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class TicketsReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.failedCode = None
        self.failedReason = None
        self.orderCode = None
        self.orderItemCode = None
        self.orderStatus = None
        self.successTime = None
        self.ticketList = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False},
        	'orderItemCode':{'allow_empty':False},
        	'orderStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiveTickets'

    def getApiMethod(self):

        return 'suning.custom.tickets.receive'



