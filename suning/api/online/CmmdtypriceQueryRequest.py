# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtypriceQueryRequest(AbstractApi):

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



