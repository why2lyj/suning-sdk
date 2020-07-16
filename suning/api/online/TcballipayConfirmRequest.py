# -*- coding: utf-8 -*-

'''

Created on 2019-4-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class TcballipayConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.tcbAlipay = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmTcballipay'

    def getApiMethod(self):

        return 'suning.online.tcballipay.confirm'



