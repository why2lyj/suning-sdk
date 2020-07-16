# -*- coding: utf-8 -*-

'''

Created on 2019-8-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class BanktransferCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderIds = None
        self.phoneNum = None
        
        self.setParamRule({
        	'phoneNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createBanktransfer'

    def getApiMethod(self):

        return 'suning.govbus.banktransfer.create'



