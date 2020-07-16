# -*- coding: utf-8 -*-

'''

Created on 2020-3-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class BacthcustomlinkQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.extend = None
        self.promotionId = None
        self.subUser = None
        
        self.setParamRule({
        	'extend':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryBacthcustomlink'

    def getApiMethod(self):

        return 'suning.netalliance.bacthcustomlink.query'



