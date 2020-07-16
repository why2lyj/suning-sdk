# -*- coding: utf-8 -*-

'''

Created on 2020-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class ThirdpartypromotionGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channel = None
        self.outerId = None
        self.promotionId = None
        self.subUser = None
        
        self.setParamRule({
        	'channel':{'allow_empty':False},
        	'outerId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getThirdpartygetpromotion'

    def getApiMethod(self):

        return 'suning.netalliance.thirdpartygetpromotion.get'



