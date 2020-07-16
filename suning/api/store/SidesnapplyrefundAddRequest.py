# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnapplyrefundAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemNoItems = None
        self.orderNo = None
        self.returnReasonCode = None
        self.returnReasonDesc = None
        
        self.setParamRule({
        	'orderNo':{'allow_empty':False},
        	'returnReasonCode':{'allow_empty':False},
        	'returnReasonDesc':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSidesnapplyrefund'

    def getApiMethod(self):

        return 'suning.store.sidesnapplyrefund.add'



