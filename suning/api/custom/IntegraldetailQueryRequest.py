# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class IntegraldetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memCode = None
        self.pageNo = None
        self.pageSize = None
        self.rightType = None
        
        self.setParamRule({
        	'memCode':{'allow_empty':False},
        	'rightType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryIntegraldetail'

    def getApiMethod(self):

        return 'suning.custom.integraldetail.query'



