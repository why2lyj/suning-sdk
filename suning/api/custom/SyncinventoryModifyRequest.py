# -*- coding: utf-8 -*-

'''

Created on 2017-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class SyncinventoryModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invCode = None
        self.invQty = None
        self.invType = None
        self.productCode = None
        
        self.setParamRule({
        	'invCode':{'allow_empty':False},
        	'invQty':{'allow_empty':False},
        	'invType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifySyncinventory'

    def getApiMethod(self):

        return 'suning.custom.syncinventory.modify'



