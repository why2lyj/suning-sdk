# -*- coding: utf-8 -*-

'''

Created on 2019-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class AddressQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.addressHierarchy = None
        self.provinceCode = None
        
        self.setParamRule({
        	'addressHierarchy':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryAddress'

    def getApiMethod(self):

        return 'suning.buyout.address.query'



