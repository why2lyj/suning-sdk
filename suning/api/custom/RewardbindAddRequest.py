# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class RewardbindAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memCode = None
        self.sourceNo = None
        
        self.setParamRule({
        	'memCode':{'allow_empty':False},
        	'sourceNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addRewardbind'

    def getApiMethod(self):

        return 'suning.custom.rewardbind.add'



