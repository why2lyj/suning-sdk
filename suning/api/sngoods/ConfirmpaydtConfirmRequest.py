# -*- coding: utf-8 -*-

'''

Created on 2020-5-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class ConfirmpaydtConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmConfirmpaydt'

    def getApiMethod(self):

        return 'suning.sngoods.confirmpaydt.confirm'



