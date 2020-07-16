# -*- coding: utf-8 -*-

'''

Created on 2019-12-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class QuerypacketQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryQuerypacket'

    def getApiMethod(self):

        return 'suning.netalliance.querypacket.query'



