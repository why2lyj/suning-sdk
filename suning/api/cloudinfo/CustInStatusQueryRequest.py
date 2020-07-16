# -*- coding: utf-8 -*-

'''

Created on 2016-11-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class CustInStatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.loginName = None
        self.searchTime = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'loginName':{'allow_empty':False},
        	'searchTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCustInStatus'

    def getApiMethod(self):

        return 'suning.cloudinfo.custinstatus.query'



