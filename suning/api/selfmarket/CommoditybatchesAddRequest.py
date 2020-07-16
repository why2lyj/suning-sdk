# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommoditybatchesAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commodityBatches = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addCommoditybatches'

    def getApiMethod(self):

        return 'suning.selfmarket.commoditybatches.add'



