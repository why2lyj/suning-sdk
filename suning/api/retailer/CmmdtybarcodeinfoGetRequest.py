# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtybarcodeinfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.barcode = None
        
        self.setParamRule({
        	'barcode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCmmdtybarcodeinfo'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtybarcodeinfo.get'



