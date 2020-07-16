# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class SeaOrderJoinAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderLineNumberList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addSeaOrderJoin'

    def getApiMethod(self):

        return 'suning.supply.seaorderjoin.add'



