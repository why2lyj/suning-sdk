# -*- coding: utf-8 -*-

'''

Created on 2020-3-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class AbcpayAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelType = None
        self.orderIds = None
        self.returnUrl = None
        
        self.setParamRule({
        	'channelType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addAbcpay'

    def getApiMethod(self):

        return 'suning.govbus.abcpay.add'



