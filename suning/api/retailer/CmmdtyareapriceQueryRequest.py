# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyareapriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.cityCode = None
        self.cmmdtyList = None
        self.districtCode = None
        self.storeCode = None
        self.townCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'cityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtyareaprice'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtyareaprice.query'



