# -*- coding: utf-8 -*-

'''

Created on 2019-10-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class AddresssetQueryRequest(AbstractApi):

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

        return 'queryAddressset'

    def getApiMethod(self):

        return 'suning.online.addressset.query'



