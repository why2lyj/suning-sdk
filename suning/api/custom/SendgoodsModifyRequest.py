# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class SendgoodsModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliveryTime = None
        self.expressCompanyCode = None
        self.expressNo = None
        self.operateStyle = None
        self.productCode = None
        self.sdcsOrderId = None
        
        self.setParamRule({
        	'expressCompanyCode':{'allow_empty':False},
        	'expressNo':{'allow_empty':False},
        	'operateStyle':{'allow_empty':False},
        	'sdcsOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifySendgoods'

    def getApiMethod(self):

        return 'suning.custom.sendgoods.modify'



