# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtypagesourcingQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.cmmdtyList = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtypagesourcing'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtypagesourcing.query'



