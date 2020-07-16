# -*- coding: utf-8 -*-

'''

Created on 2020-3-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoredeclareinformationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.packageOrderId = None
        
        self.setParamRule({
        	'packageOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryStoredeclareinformation'

    def getApiMethod(self):

        return 'suning.custom.storedeclareinformation.query'



