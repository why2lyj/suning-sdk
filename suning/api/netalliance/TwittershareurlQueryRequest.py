# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class TwittershareurlQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsNo = None
        
        self.setParamRule({
        	'goodsNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryTwittershareurl'

    def getApiMethod(self):

        return 'suning.netalliance.twittershareurl.query'



