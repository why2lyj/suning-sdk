# -*- coding: utf-8 -*-

'''

Created on 2020-2-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderlogistGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderlogist'

    def getApiMethod(self):

        return 'suning.sngoods.orderlogist.get'



