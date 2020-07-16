# -*- coding: utf-8 -*-

'''

Created on 2016-1-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class SeaOrderDeclareAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.b2cOrderNo = None
        self.orderLineList = None
        
        self.setParamRule({
        	'b2cOrderNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addSeaOrderDeclare'

    def getApiMethod(self):

        return 'suning.custom.seaorderdeclare.add'



