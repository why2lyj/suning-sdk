# -*- coding: utf-8 -*-

'''

Created on 2018-3-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class childItemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.alertQty = None
        self.barcode = None
        self.barpic = None
        self.deductiblePriceChild = None
        self.invQty = None
        self.itemCode = None
        self.parentProductCode = None
        self.pars = None
        self.price = None
        self.supplierImg1Url = None
        self.pingouPrice = None
        
        self.setParamRule({
        	'parentProductCode':{'allow_empty':False},
        	'pingouPrice':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'childItem'

    def getApiMethod(self):

        return 'suning.integrate.childitem.add'



