# -*- coding: utf-8 -*-

'''

Created on 2018-8-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class CustomercheckGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.psptFrontImage = None
        self.psptBackImage = None
        self.faceImage = None
        
        self.setParamRule({
        	'psptFrontImage':{'allow_empty':False},
        	'psptBackImage':{'allow_empty':False},
        	'faceImage':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCustomercheck'

    def getApiMethod(self):

        return 'suning.operasale.customercheck.get'



