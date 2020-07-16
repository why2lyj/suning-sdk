# -*- coding: utf-8 -*-

'''

Created on 2018-5-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class BjcpmmurlGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionId = None
        
        self.setParamRule({
        	'promotionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getBjcpmmurl'

    def getApiMethod(self):

        return 'suning.advertise.bjcpmmurl.get'



