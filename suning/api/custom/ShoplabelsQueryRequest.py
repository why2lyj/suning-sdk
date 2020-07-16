# -*- coding: utf-8 -*-

'''

Created on 2018-9-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShoplabelsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryShoplabels'

    def getApiMethod(self):

        return 'suning.custom.shoplabels.query'



