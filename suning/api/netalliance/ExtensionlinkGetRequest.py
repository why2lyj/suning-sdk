# -*- coding: utf-8 -*-

'''

Created on 2019-9-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExtensionlinkGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productUrl = None
        self.promotionId = None
        self.quanUrl = None
        self.subUser = None
        
        self.setParamRule({
        	'productUrl':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getExtensionlink'

    def getApiMethod(self):

        return 'suning.netalliance.extensionlink.get'



