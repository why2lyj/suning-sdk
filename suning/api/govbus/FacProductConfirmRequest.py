# -*- coding: utf-8 -*-

'''

Created on 2017-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class FacProductConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.skuConfirmList = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'confirmFacProduct'

    def getApiMethod(self):

        return 'suning.govbus.facproduct.confirm'



