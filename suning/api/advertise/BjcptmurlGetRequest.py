# -*- coding: utf-8 -*-

'''

Created on 2018-5-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class BjcptmurlGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionId = None
        
        self.setParamRule({
        	'promotionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getBjcptmurl'

    def getApiMethod(self):

        return 'suning.advertise.bjcptmurl.get'



