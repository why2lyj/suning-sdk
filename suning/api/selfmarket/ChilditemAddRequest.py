# -*- coding: utf-8 -*-

'''

Created on 2017-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChilditemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.parentProductCode = None
        self.pars = None
        self.supplierImgAUrl = None
        self.itemCode = None
        self.barcode = None
        self.barpic = None
        
        self.setParamRule({
        	'parentProductCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addChilditem'

    def getApiMethod(self):

        return 'suning.selfmarket.childitem.add'



