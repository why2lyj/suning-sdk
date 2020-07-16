# -*- coding: utf-8 -*-

'''

Created on 2020-4-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class MycommodityselectgroupQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageIndex = None
        self.size = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryMycommodityselectgroup'

    def getApiMethod(self):

        return 'suning.netalliance.mycommodityselectgroup.query'



