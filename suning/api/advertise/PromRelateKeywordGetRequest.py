# -*- coding: utf-8 -*-

'''

Created on 2016-11-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromRelateKeywordGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.keyword = None
        
        self.setParamRule({
        	'keyword':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPromRelateKeyword'

    def getApiMethod(self):

        return 'suning.advertise.promrelatekeyword.get'



