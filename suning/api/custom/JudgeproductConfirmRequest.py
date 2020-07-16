# -*- coding: utf-8 -*-

'''

Created on 2017-6-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class JudgeproductConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.cmBarcode = None
        self.fixedPrice = None
        self.productName = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	'productName':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmJudgeproduct'

    def getApiMethod(self):

        return 'suning.custom.judgeproduct.confirm'



