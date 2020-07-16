# -*- coding: utf-8 -*-

'''

Created on 2018-1-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class FactoryinventoryModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commodityList = None
        self.invType = None
        
        self.setParamRule({
        	'invType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyFactoryinventory'

    def getApiMethod(self):

        return 'suning.oto.factoryinventory.modify'



