# -*- coding: utf-8 -*-

'''

Created on 2017-9-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class CategoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getCategory'

    def getApiMethod(self):

        return 'suning.govbus.category.get'



