# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BatchsettlementQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryBatchsettlement'

    def getApiMethod(self):

        return 'suning.online.batchsettlement.query'



