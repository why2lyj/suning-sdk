# -*- coding: utf-8 -*-

'''

Created on 2015-6-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChildUserInfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.mainCust = None
        self.keyword = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryChildUserInfo'

    def getApiMethod(self):

        return 'suning.cloud.childuserinfo.query'



