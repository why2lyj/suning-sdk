# -*- coding: utf-8 -*-

'''

Created on 2016-8-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemInfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryItemInfo'

    def getApiMethod(self):

        return 'suning.fourps.iteminfo.query'



