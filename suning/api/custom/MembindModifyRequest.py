# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class MembindModifyRequest(AbstractApi):

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

        return 'modifyMembind'

    def getApiMethod(self):

        return 'suning.custom.membind.modify'



