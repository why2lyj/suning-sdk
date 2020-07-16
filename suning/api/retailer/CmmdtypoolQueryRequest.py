# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtypoolQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.distributorCode = None
        self.pnumber = None
        self.psize = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'pnumber':{'allow_empty':False},
        	'psize':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtypool'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtypool.query'



