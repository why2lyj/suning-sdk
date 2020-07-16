# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class SeaOrderDeclareAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.packageOrderId = None
        
        self.setParamRule({
        	'packageOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSeaOrderDeclare'

    def getApiMethod(self):

        return 'suning.supply.seaorderdeclare.add'



