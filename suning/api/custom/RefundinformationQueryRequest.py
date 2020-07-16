# -*- coding: utf-8 -*-

'''

Created on 2020-5-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundinformationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.returnApplyId = None
        
        self.setParamRule({
        	'returnApplyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRefundinformation'

    def getApiMethod(self):

        return 'suning.custom.refundinformation.query'



