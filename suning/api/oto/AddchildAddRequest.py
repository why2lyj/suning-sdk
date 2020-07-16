# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class AddchildAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.parentProductCode = None
        self.itemCode = None
        self.barcode = None
        self.price = None
        self.barpic = None
        self.supplierImg1Url = None
        self.pars = None
        
        self.setParamRule({
        	'parentProductCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addAddchild'

    def getApiMethod(self):

        return 'suning.oto.addchild.add'



