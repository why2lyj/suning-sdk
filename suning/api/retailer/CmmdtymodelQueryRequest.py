# -*- coding: utf-8 -*-

'''

Created on 2020-4-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtymodelQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyCodes = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtymodel'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtymodel.query'



