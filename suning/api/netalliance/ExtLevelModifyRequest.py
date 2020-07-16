# -*- coding: utf-8 -*-

'''

Created on 2016-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExtLevelModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.mixCustNum = None
        self.extSystemId = None
        self.extLevel = None
        self.isPayMember = None
        
        self.setParamRule({
        	'mixCustNum':{'allow_empty':False},
        	'extSystemId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyExtLevel'

    def getApiMethod(self):

        return 'suning.netalliance.extlevel.modify'



