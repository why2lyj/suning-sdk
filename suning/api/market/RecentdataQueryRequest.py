# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class RecentdataQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRecentdata'

    def getApiMethod(self):

        return 'suning.market.recentdata.query'



