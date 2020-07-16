# -*- coding: utf-8 -*-

'''

Created on 2017-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class WarepooldistrictagingQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityCode = None
        self.warehouseCode = None
        
        self.setParamRule({
        	'cityCode':{'allow_empty':False},
        	'warehouseCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryWarepooldistrictaging'

    def getApiMethod(self):

        return 'suning.oto.warepooldistrictaging.query'



