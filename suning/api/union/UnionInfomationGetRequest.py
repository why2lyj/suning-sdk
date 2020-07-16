# -*- coding: utf-8 -*-

'''

Created on 2016-1-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnionInfomationGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsCode = None
        
        self.setParamRule({
        	'goodsCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getUnionInfomation'

    def getApiMethod(self):

        return 'suning.netalliance.unioninfomation.get'



