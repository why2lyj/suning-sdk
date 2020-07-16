# -*- coding: utf-8 -*-

'''

Created on 2017-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class WarepoolcityagingQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        
        self.setParamRule({
        	'warehouseCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryWarepoolcityaging'

    def getApiMethod(self):

        return 'suning.oto.warepoolcityaging.query'



