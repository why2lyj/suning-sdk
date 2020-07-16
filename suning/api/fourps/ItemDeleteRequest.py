# -*- coding: utf-8 -*-

'''

Created on 2015-12-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCmCode = None
        
        self.setParamRule({
        	'supplierCmCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteItem'

    def getApiMethod(self):

        return 'suning.fourps.item.delete'



