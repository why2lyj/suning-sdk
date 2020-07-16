# -*- coding: utf-8 -*-

'''

Created on 2019-9-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class HomepagepositionurlQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.subUser = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryHomepagepositionurl'

    def getApiMethod(self):

        return 'suning.netalliance.homepagepositionurl.query'



