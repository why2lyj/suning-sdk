# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnionInfomationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.adBookId = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'adBookId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryUnionInfomation'

    def getApiMethod(self):

        return 'suning.netalliance.unioninfomation.query'



