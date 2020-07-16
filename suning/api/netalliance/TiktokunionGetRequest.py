# -*- coding: utf-8 -*-

'''

Created on 2019-9-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class TiktokunionGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channel = None
        self.outerId = None
        self.statParam = None
        
        self.setParamRule({
        	'channel':{'allow_empty':False},
        	'outerId':{'allow_empty':False},
        	'statParam':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getTiktokgetunion'

    def getApiMethod(self):

        return 'suning.netalliance.tiktokgetunion.get'



