# -*- coding: utf-8 -*-

'''

Created on 2019-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class BuysuperAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appCode = None
        self.businessSource = None
        self.goodsNoConfigId = None
        self.mixCustNum = None
        self.packageType = None
        self.phone = None
        self.seqId = None
        
        self.setParamRule({
        	'appCode':{'allow_empty':False},
        	'mixCustNum':{'allow_empty':False},
        	'seqId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addBuysuper'

    def getApiMethod(self):

        return 'suning.superext.buysuper.add'



