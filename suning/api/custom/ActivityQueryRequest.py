# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryActivity'

    def getApiMethod(self):

        return 'suning.custom.activity.query'



