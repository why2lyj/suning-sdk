# -*- coding: utf-8 -*-

'''

Created on 2019-4-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class TcbwechatpayConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.tcbwechatpay = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmTcbwechatpay'

    def getApiMethod(self):

        return 'suning.online.tcbwechatpay.confirm'



