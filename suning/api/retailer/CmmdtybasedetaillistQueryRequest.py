# -*- coding: utf-8 -*-

'''

Created on 2020-4-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtybasedetaillistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyBaseQueryDTOs = None
        self.platformCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtybasedetaillist'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtybasedetaillist.query'



