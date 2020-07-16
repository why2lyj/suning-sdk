# -*- coding: utf-8 -*-

'''

Created on 2018-12-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyInfo = None
        self.sceneType = None
        
        self.setParamRule({
        	'sceneType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtyprice'

    def getApiMethod(self):

        return 'suning.online.price.query'



