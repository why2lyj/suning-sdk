# -*- coding: utf-8 -*-

'''

Created on 2018-12-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class SetsecretkeyUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.publicKey = None
        self.type = None
        
        self.setParamRule({
        	'publicKey':{'allow_empty':False},
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateSetsecretkey'

    def getApiMethod(self):

        return 'suning.govbus.setsecretkey.update'



