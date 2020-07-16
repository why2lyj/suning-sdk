# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class ParamtemplateQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryParamtemplate'

    def getApiMethod(self):

        return 'suning.store.paramtemplate.query'



