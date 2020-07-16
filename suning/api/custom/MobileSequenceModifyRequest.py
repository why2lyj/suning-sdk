# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class MobileSequenceModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.moduleInfo = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'modifyMobileSequence'

    def getApiMethod(self):

        return 'suning.custom.mobilesequence.modify'



