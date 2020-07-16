# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtysimilarQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cityCode = None
        self.cmmdtyCode = None
        self.distributorCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'cityCode':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'distributorCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtysimilar'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtysimilar.query'



