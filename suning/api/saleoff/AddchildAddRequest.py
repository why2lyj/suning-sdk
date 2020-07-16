# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class AddchildAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.barpic = None
        self.pars = None
        self.itemCode = None
        self.supplierImgUrlA = None
        self.price = None
        self.parentProductCode = None
        self.barcode = None
        
        self.setParamRule({
        	'parentProductCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addAddchild'

    def getApiMethod(self):

        return 'suning.saleoff.addchild.add'



