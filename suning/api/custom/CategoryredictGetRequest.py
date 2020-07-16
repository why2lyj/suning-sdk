# -*- coding: utf-8 -*-

'''

Created on 2017-11-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CategoryredictGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmTitle = None
        self.categoryCode = None
        
        self.setParamRule({
        	'cmTitle':{'allow_empty':False},
        	'categoryCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCategoryredict'

    def getApiMethod(self):

        return 'suning.custom.categoryredict.get'



