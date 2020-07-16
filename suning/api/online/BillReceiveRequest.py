# -*- coding: utf-8 -*-

'''

Created on 2020-1-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class BillReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.billDetailReqItemList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'receiveBill'

    def getApiMethod(self):

        return 'suning.online.bill.receive'



