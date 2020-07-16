# -*- coding: utf-8 -*-

'''

Created on 2019-12-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductoperateAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channel = None
        self.custNum = None
        self.entrance = None
        self.mdmCityCode = None
        self.partnumber = None
        self.pdType = None
        self.shopId = None
        self.shoptType = None
        
        self.setParamRule({
        	'channel':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'entrance':{'allow_empty':False},
        	'mdmCityCode':{'allow_empty':False},
        	'partnumber':{'allow_empty':False},
        	'pdType':{'allow_empty':False},
        	'shopId':{'allow_empty':False},
        	'shoptType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addProductoperate'

    def getApiMethod(self):

        return 'suning.custom.productoperate.add'



