# -*- coding: utf-8 -*-

'''

Created on 2019-12-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class AlipayCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.backUrl = None
        self.channelType = None
        self.mobileModel = None
        self.mobileOS = None
        self.orderIds = None
        
        self.setParamRule({
        	'channelType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createAlipay'

    def getApiMethod(self):

        return 'suning.govbus.alipay.create'



