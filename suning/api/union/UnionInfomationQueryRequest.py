# -*- coding: utf-8 -*-

'''

Created on 2015-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnionInfomationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryUnionInfomation'

    def getApiMethod(self):

        return 'suning.netalliance.unioninfomation.query'



