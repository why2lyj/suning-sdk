# -*- coding: utf-8 -*-

'''

Created on 2016-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SnMemberLevelGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.extSystemId = None
        self.mixCustNum = None
        
        self.setParamRule({
        	'extSystemId':{'allow_empty':False},
        	'mixCustNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSnMemberLevel'

    def getApiMethod(self):

        return 'suning.netalliance.snmemberlevel.get'



