# -*- coding: utf-8 -*-

'''

Created on 2019-8-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChannelcommodityGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.backUrl = None
        self.channelCode = None
        self.custNum = None
        self.visitUrl = None
        
        self.setParamRule({
        	'backUrl':{'allow_empty':False},
        	'channelCode':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'visitUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getChannelcommodity'

    def getApiMethod(self):

        return 'suning.netalliance.channelcommodity.get'



