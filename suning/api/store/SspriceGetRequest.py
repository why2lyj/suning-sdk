# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SspriceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.appStoreCode = None
        self.currentPage = None
        self.pageNum = None
        self.storeCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'currentPage':{'allow_empty':False},
        	'pageNum':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getSsprice'

    def getApiMethod(self):

        return 'suning.store.ssprice.get'



