# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class IdentifyresultConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.isAll = None
        self.serialList = None
        self.tripCode = None
        
        self.setParamRule({
        	'isAll':{'allow_empty':False},
        	'tripCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmIdentifyresult'

    def getApiMethod(self):

        return 'suning.defctive.identifyresult.confirm'



