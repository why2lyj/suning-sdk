# -*- coding: utf-8 -*-

'''

Created on 2018-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoregroupQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.groupCode = None
        self.groupName = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryStoregroup'

    def getApiMethod(self):

        return 'suning.custom.storegroup.query'



