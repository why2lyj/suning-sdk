# -*- coding: utf-8 -*-

'''

Created on 2020-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoselfpinkupQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOtoselfpinkup'

    def getApiMethod(self):

        return 'suning.onlinestore.selfpinkup.query'



